require 'open-uri'
require 'nokogiri'
require 'pp'


EMAIL_REGEX = /\b[A-Z0-9._%a-z\-]+@(?:[A-Z0-9a-z\-]+\.)+[A-Za-z]{2,4}/
COMPANIES = {}
MAILS = {}
ERRORS = []
file = File.new('./parsed_emails.csv', 'w')

def request_post(v)
  html = Nokogiri::HTML(open(v))
  html.css('.post.type-post.status-publish').to_s
rescue
  puts "!!!!!!!!! link #{v} is failed | 2 cycle"
end

def request_page(url)
  html = Nokogiri::HTML(open(url))
  link = html.css('.indextitle a')
rescue
  puts "!!!!!!!!! link #{url} is failed | 1 cycle"
end

1.upto(1) do |page_number|
  if page_number == 1
    url = "http://www.topinteractiveagencies.com/digital-directory/europe/"
  else
    url = "http://www.topinteractiveagencies.com/digital-directory/europe/page/#{page_number}/"
  end

  link = request_page(url)

  link.map do |page|
    company = {page.text.strip => page['href']}
    COMPANIES.update(company)
  end
end

COMPANIES.each do |k,v|
  post = request_post(v)

  ERRORS << 'error' if (post == "" && post == nil)

  post_mails = post.scan(EMAIL_REGEX).uniq
  MAILS.update({k => post_mails})
end

MAILS.each do |k,v|
  v.each do |email|
    file << "#{k};#{email}\n"
  end
end

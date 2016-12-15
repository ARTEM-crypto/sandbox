require "watir"
require "csv"


accounts = File.open(ARGV[0])

n = 1

CSV.foreach(accounts) do |row|
  begin
    p row
    p n
    n += 1

    if  row[1] == nil
      next
    end

    browser =  Watir::Browser.new :phantomjs
    browser.goto 'https://lkfl.nalog.ru/lk/index.html'

    browser.text_field(id: 'logonForm_username').set row[0]
    browser.text_field(id: 'logonForm_password').set row[1]
    browser.button(:id => 'logonForm_submit').click

    sleep 2
    if browser.html.include?("Неправильный пароль.") || browser.html.include?("Срок действия первичного пароля (1 месяц)")
      p ('error: ' + row[0])
      browser.close
      next
    end

    browser.text_field(id: 'profileForm_curPwd').set(row[1])
    browser.text_field(id: 'profileForm_newPwd').set(row[1]+ '3')
    browser.text_field(id: 'profileForm_newPwd2').set(row[1] + '3')
    browser.button(:id => 'profileForm_submit').click

    browser.close
  rescue
    browser.close
    p 'error: ' + row[0]
    next
  end
end

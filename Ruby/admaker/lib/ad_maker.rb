require "bundler/setup"
Bundler.require
require 'capybara/dsl'
require_relative "capybara_with_phantom_js"

class AdMaker
  include CapybaraWithPhantomJs

  p CapybaraWithPhantomJs

  MYTARGET_URL = "https://target.my.com/"

  def initialize(eamil, password, app_name)
    @email = eamil
    @password = password
    @app_name = app_name
  end

  def login
    new_session
    visit MYTARGET_URL
    sleep 5
    p html
  end

  def self.create_adunits
    puts "Please enter email"
    email = STDIN.gets.chomp
    puts "Please enter password"
    password = STDIN.gets.chomp
    puts "Please enter application name"
    app_name = STDIN.gets.chomp

    client = new(email, password, app_name)
    client.login
    nil
  end
end

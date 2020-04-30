// Generated by Selenium IDE
const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')

describe('test_baidu_search', function() {
  this.timeout(30000)
  let driver
  let vars
  beforeEach(async function() {
    driver = await new Builder().forBrowser('firefox').build()
    vars = {}
  })
  afterEach(async function() {
    await driver.quit();
  })
  it('test_baidu_search', async function() {
    await driver.get("https://www.baidu.com/")
    await driver.manage().window().setRect(1464, 791)
    await driver.findElement(By.id("kw")).click()
    await driver.findElement(By.id("kw")).sendKeys("selenium ide")
    await driver.findElement(By.id("kw")).sendKeys(Key.ENTER)
  })
})

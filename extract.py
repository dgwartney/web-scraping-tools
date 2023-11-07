#!/usr/bin/env python3
import asyncio
from pyppeteer import launch

#defining an async method
async def main():
    # launching browser session
    browser = await launch( )
    # opening a new page
    page = await browser.newPage()
    # go to a specific address or file
    await page.goto('https://help.calendly.com/hc/en-us/articles/223195448-Manage-your-account-settings-an-overview')
    #create a screen shot from the page
    await page.screenshot({'path': 'sample.png'})
    # save the screenshot as a pdf
    await page.pdf({'path': 'pyppeteer_pdf.pdf'})
    #close the browser
    await browser.close()
# invocation of the Async main function
asyncio.get_event_loop().run_until_complete(main())

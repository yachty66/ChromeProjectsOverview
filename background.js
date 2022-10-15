function hideProfiles() {
  [].forEach.call(document.querySelectorAll('.user-info '), function (el) {
    el.style.visibility = 'hidden';
  });
}

chrome.tabs.onUpdated.addListener((tabId, tab) => {
  if (tab.url) {
    if (tab.url.includes("stackoverflow.com")) {
      console.log("StackOverflow");
      chrome.scripting.executeScript({
        target: { tabId: tabId },
        func: hideProfiles,
      })
    }
  }
});

//now I need to make regularly requests to my home.md and I need to scrape every header from currently doing and  

//if new tab was created i just need to do something like setting background 

//can create js file which is scraping every heeader
//add header in index.html 
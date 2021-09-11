// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// To make sure we can uniquely identify each screenshot tab, add an id as a
// query param to the url that displays the screenshot.
// Note: It's OK that this is a global variable (and not in localStorage),
// because the event page will stay open as long as any screenshot tabs are
// open.

// Listen for a click on the camera icon. On that click, take a screenshot.
chrome.browserAction.onClicked.addListener(function () {
  chrome.tabs.captureVisibleTab(async function (screenshotUrl) {
    const formData = new FormData();
    formData.append("file", screenshotUrl);

<<<<<<< HEAD
  chrome.tabs.captureVisibleTab(async function(screenshotUrl) {
      const formData = new FormData();
      formData.append('file', screenshotUrl);

      try {
        const data = await fetch('http://localhost:8000/', {
          method: 'POST',
          headers: {
            'Content-Type': 'multipart/form-data',
          },
          body: formData,
        });
        const response = await data.json();
        console.log(response);
        console.log(data);

      } catch (err) {
        console.log(err);
      }
=======
    fetch("http://localhost:8000/", {
      method: "POST",
      headers: {},
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => console.log(data))
      .catch(err => console.log(err))
>>>>>>> 66ea38bf496be342b6b9e33c2957b836f495381d
  });
});

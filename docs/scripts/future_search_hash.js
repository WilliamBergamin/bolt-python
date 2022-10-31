var searchTag = "details";

window.addEventListener("hashchange", (event) => {
  const hash = location.hash.substring(1);
  if (!hash) return;
  const details = document.getElementsByTagName(searchTag);
  for (let i = 0; i < details.length; i++) {
    if (details[i].querySelector(`#${hash}`)) {
      details[i].open = true;
      window.location.hash = `#${hash}`;
      break;
    }
  }
});

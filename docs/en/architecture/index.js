function filterDocs() {
  const checkboxes = document.querySelectorAll('.filter-tags input[type="checkbox"]');
  const tags = Array.from(checkboxes)
    .filter(cb => cb.checked)
    .map(cb => cb.value);

  const entries = document.querySelectorAll('.doc-entry');
  entries.forEach(entry => {
    const entryTags = entry.dataset.tags;
    entry.style.display = (tags.length === 0 || tags.some(tag => entryTags.includes(tag))) ? 'list-item' : 'none';
  });
}

// Auto-hook checkboxes
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('.filter-tags input').forEach(cb => {
    cb.addEventListener("change", filterDocs);
  });
});

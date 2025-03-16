document.addEventListener('DOMContentLoaded', function () {
    const categoryDropdown = document.querySelector('select[name="category"]');
    const otherCategoryInput = document.getElementById('other-category-container');
  
    categoryDropdown.addEventListener('change', function () {
      if (categoryDropdown.value === 'Other') {
        otherCategoryInput.style.display = 'block';  // Show the "Other" category input
      } else {
        otherCategoryInput.style.display = 'none';  // Hide the "Other" category input
      }
    });
  });
  
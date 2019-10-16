---
layout: page
title: "Publications"
---

<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search...">

{% for yr in (1998..2025) reversed %}
{% include publications.html year=yr %}
{% endfor %}


<script>
function myFunction() {
  // Declare variables
  var input, filter, table, ul, li, i, txtValue, year;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();

  for (year = 1998; year <= 2025; year++) {
	  ul = document.getElementById("papers_" + year); 
	  if (ul) {
	  li = ul.getElementsByTagName("li");

	  for (i = 0; i < li.length; i++) {
	    txtValue = li[i].textContent || li[i].innerText;
	    if (txtValue.toUpperCase().indexOf(filter) > -1) {
		    li[i].style.display = "";
	    } else {
		    li[i].style.display = "none";
	    }
	  }
      }
  }
}
</script>


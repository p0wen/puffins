$(document).ready(function () {
  let menuExtended = false;
  let scrollPosition;
  // Scroll Animation based on 2 sources https://www.w3schools.com/js/tryit.asp?filename=tryjs_intro_lightbulb , https://www.youtube.com/watch?v=vE4UuSzR5T0
  window.addEventListener("scroll", function () {
    let navbar = document.querySelector("nav");
    document.getElementById("#puffinName");
    scrollPosition = window.scrollY > 0;
    if (scrollPosition) {
      if ($("nav").hasClass("scrolling-active")) {
        // do nothing
      } else {
        $("nav").addClass("scrolling-active");
        $("#puffinName").attr("src", url_puffin_dark);
      }
    } else {
      if ($("nav").hasClass("scrolling-active") && menuExtended) {
        // do nothing
      } else {
        $("nav").removeClass("scrolling-active");
        $("#puffinName").attr("src", url_puffin_light);
      }
    }
  });

  // Takes Care of Navigation when collapsed and not scrolled adapted form here : https://stackoverflow.com/questions/32147082/changing-collapsed-navbar-list-background-color

  $(".navbar-toggler").click(function () {
    if (!scrollPosition & !menuExtended) {
      $("nav").addClass("scrolling-active");
      $("#puffinName").attr("src", url_puffin_dark);
      menuExtended = true;
    } else if (scrollPosition & menuExtended) {
      menuExtended = false;
    } else if (scrollPosition & !menuExtended) {
      $("nav").addClass("scrolling-active");
      $("#puffinName").attr("src", url_puffin_dark);
      menuExtended = true;
    } else if (!scrollPosition & menuExtended) {
      $("nav").removeClass("scrolling-active", menuExtended);
      $("#puffinName").attr("src", url_puffin_light);
      menuExtended = false;
    } else {
    }
  });

  // Get the CartSideDrawer
  $("#cart-open").click(function () {
    openSideCart();
  });

  // Close CartSideDrawer
  $(document).on("click", "#overlay", closeSideCart);

  /**
   * Fix Viewport for mobile browser taken from own zengarden project / origin of solution (https://dev.to/admitkard/mobile-issue-with-100vh-height-100-100vh-3-solutions-3nae)
   */

  // Call resize view on page load to have correct vh
  resizeView();

  // Update vh variable on screen resize
  window.addEventListener("resize", () => {
    resizeView();
  });

  // Check innerHeight of window to adjust for mobile view with task bars
  function resizeView() {
    let root = document.querySelector(":root");
    root.style.setProperty("--vh", window.innerHeight / 100 + "px");
  }
});

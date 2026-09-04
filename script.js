(function () {
    "use strict";

    const loader = document.querySelector(".loader");
    const progress = document.querySelector(".progress");
    const cursorSmall = document.querySelector(".cursor-small");
    const cursorLarge = document.querySelector(".cursor-large");
    const sections = document.querySelectorAll(".story-section");
    const navDots = document.querySelectorAll(".nav-dot");
    const marquee = document.querySelector(".hero-marquee");
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function setProgress() {
        if (!progress) return;
        const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
        const percentage = scrollableHeight > 0 ? (window.scrollY / scrollableHeight) * 100 : 0;
        progress.style.width = `${percentage}%`;
    }

    function setActiveSection() {
        let activeIndex = 0;
        sections.forEach((section, index) => {
            if (section.getBoundingClientRect().top <= window.innerHeight * 0.35) {
                activeIndex = index;
            }
        });
        navDots.forEach((dot, index) => dot.classList.toggle("active", index === activeIndex));
    }

    window.addEventListener("scroll", () => {
        setProgress();
        setActiveSection();
    }, { passive: true });

    setProgress();
    setActiveSection();

    if (loader) {
        window.addEventListener("load", () => {
            loader.style.transition = "opacity 0.6s ease, visibility 0.6s ease";
            loader.style.opacity = "0";
            loader.style.visibility = "hidden";
        }, { once: true });
    }

    if (marquee && !reducedMotion) {
        const marqueeAnimation = marquee.animate(
            [{ transform: "translateX(0)" }, { transform: "translateX(-35%)" }],
            { duration: 18000, iterations: Infinity, easing: "linear" },
        );
        window.addEventListener("blur", () => marqueeAnimation.pause());
        window.addEventListener("focus", () => marqueeAnimation.play());
    }

    if (cursorSmall && cursorLarge && !reducedMotion && window.matchMedia("(pointer: fine)").matches) {
        window.addEventListener("pointermove", (event) => {
            cursorSmall.style.left = `${event.clientX}px`;
            cursorSmall.style.top = `${event.clientY}px`;
            cursorLarge.style.left = `${event.clientX}px`;
            cursorLarge.style.top = `${event.clientY}px`;
        });

        document.querySelectorAll(".cursor-target, .magnetic").forEach((target) => {
            target.addEventListener("mouseenter", () => cursorLarge.classList.add("hover"));
            target.addEventListener("mouseleave", () => cursorLarge.classList.remove("hover"));
        });
    }
})();

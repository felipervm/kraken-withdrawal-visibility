/* GSAP 3.15 + ScrollTrigger: accessible cinematic scroll-led motion.
   Tailwind is used for layout utilities in the image gallery. */
(() => {
  "use strict";
  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (prefersReduced.matches || !window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);
  gsap.defaults({ ease: "power3.out" });

  // Reveal the original case-study illustrations and the new two-image gallery.
  // Animations aren't dependent on a specific class being set before page load.
  const images = gsap.utils.toArray(".motion-project-image");
  if (images.length) {
    gsap.set(images, { autoAlpha: 0, scale: 1.19, transformOrigin: "50% 50%" });
    const groups = gsap.utils.toArray(".motion-image-group");
    groups.forEach((group) => {
      const items = gsap.utils.toArray(".motion-project-image", group);
      gsap.to(items, {
        autoAlpha: 1,
        scale: 1,
        duration: 1.65,
        ease: "power3.out",
        stagger: { each: 0.22, from: "start" },
        clearProps: "opacity,visibility",
        scrollTrigger: {
          trigger: group,
          start: "top 88%",
          once: true,
          invalidateOnRefresh: true
        }
      });
    });
  }

  // Section-by-section reveal, delayed sequentially but without interrupting reading.
  gsap.utils.toArray(".motion-story-group").forEach((group) => {
    const items = gsap.utils.toArray(".motion-story-item", group);
    if (!items.length) return;
    gsap.from(items, {
      autoAlpha: 0,
      y: 42,
      duration: 1.05,
      stagger: 0.13,
      ease: "power3.out",
      immediateRender: false,
      scrollTrigger: { trigger: group, start: "top 84%", once: true }
    });
  });

  // Gentle continuous scale based on scroll position. The entrance tween finishes
  // first; this targets only the image wrapper to avoid competing transforms.
  gsap.utils.toArray(".motion-parallax-shell").forEach((shell) => {
    gsap.fromTo(shell,
      { yPercent: -3 },
      { yPercent: 3, ease: "none", scrollTrigger: {
        trigger: shell, start: "top bottom", end: "bottom top", scrub: 1.4
      }}
    );
  });

  // Keep primary content visible when scripts fail or the user turns motion off.
  const killIfReduced = (event) => {
    if (!event.matches) return;
    ScrollTrigger.getAll().forEach((trigger) => trigger.kill());
    gsap.globalTimeline.clear();
    gsap.set(".motion-project-image,.motion-story-item,.motion-parallax-shell", {
      clearProps: "all"
    });
  };
  prefersReduced.addEventListener?.("change", killIfReduced);
  window.addEventListener("load", () => ScrollTrigger.refresh(), { once: true });
})();

/**
 * Lukas Sicherheitstechnik - Hero Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('mobileToggle');
  const mobileMenu = document.getElementById('mobileMenu');

  if (toggleBtn && mobileMenu) {
    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = mobileMenu.classList.toggle('open');
      toggleBtn.classList.toggle('open', isOpen);
      toggleBtn.setAttribute('aria-expanded', isOpen.toString());
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!mobileMenu.contains(e.target) && !toggleBtn.contains(e.target)) {
        mobileMenu.classList.remove('open');
        toggleBtn.classList.remove('open');
        toggleBtn.setAttribute('aria-expanded', 'false');
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('open')) {
        mobileMenu.classList.remove('open');
        toggleBtn.classList.remove('open');
        toggleBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Scroll Reveal Intersection Observer for all sections
  const animElements = document.querySelectorAll('.about-anim, .services-anim, .why-anim, .process-anim, .security-anim, .testimonials-anim, .service-area-anim, .cta-anim, .footer-anim, .about-hero-anim, .company-anim, .values-anim, .personal-anim, .services-hero-anim, .locksmith-anim, .security-tech-anim, .solutions-anim, .pricing-hero-anim, .pricing-anim, .transparency-anim, .notices-anim, .contact-hero-anim, .contact-anim, .contact-final-cta-section');
  if (animElements.length > 0) {
    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -80px 0px',
      threshold: 0.15
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    animElements.forEach((el) => {
      revealObserver.observe(el);
    });
  }

  // Timeline Step Rows & Active Node Observer
  const timelineRows = document.querySelectorAll('.timeline-step-row');
  if (timelineRows.length > 0) {
    const stepObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('step-in-view');
          const node = entry.target.querySelector('.timeline-node');
          if (node) node.classList.add('is-active');
        }
      });
    }, { threshold: 0.2, rootMargin: '0px 0px -40px 0px' });

    timelineRows.forEach(row => stepObserver.observe(row));
  }

  // Progressive Scroll-linked Timeline Line Fill
  const timelineSec = document.getElementById('ablauf');
  const lineProgress = document.querySelector('.timeline-line-progress');
  if (timelineSec && lineProgress && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const updateTimelineProgress = () => {
      const rect = timelineSec.getBoundingClientRect();
      const windowH = window.innerHeight;
      const start = windowH * 0.75;
      const totalDist = rect.height - windowH * 0.2;
      const currentDist = start - rect.top;
      let progress = currentDist / totalDist;
      if (progress < 0) progress = 0;
      if (progress > 1) progress = 1;
      lineProgress.style.height = `${(progress * 100).toFixed(1)}%`;
    };
    window.addEventListener('scroll', updateTimelineProgress, { passive: true });
    window.addEventListener('resize', updateTimelineProgress, { passive: true });
    updateTimelineProgress();
  }

  // Service Area Section Observer for sequence triggers
  const serviceAreaSec = document.getElementById('service-area');
  if (serviceAreaSec) {
    const secObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          serviceAreaSec.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    secObserver.observe(serviceAreaSec);
  }

  // Interactive Map Hotspot tooltips
  const hotspots = document.querySelectorAll('.map-hotspot');
  hotspots.forEach((hs) => {
    hs.addEventListener('mouseenter', () => {
      hotspots.forEach(other => other !== hs && other.classList.remove('active'));
      hs.classList.add('active');
    });
    hs.addEventListener('focus', () => {
      hotspots.forEach(other => other !== hs && other.classList.remove('active'));
      hs.classList.add('active');
    });
    hs.addEventListener('mouseleave', () => {
      hs.classList.remove('active');
    });
    hs.addEventListener('blur', () => {
      hs.classList.remove('active');
    });
  });

  // Testimonials Carousel Controls
  const btnPrev = document.getElementById('btnPrevTestimonial');
  const btnNext = document.getElementById('btnNextTestimonial');
  const reviewText = document.getElementById('featuredReviewText');
  const reviewName = document.getElementById('featuredName');
  const reviewAvatar = document.getElementById('featuredAvatar');
  const counter = document.getElementById('testimonialCounter');
  const progressFill = document.getElementById('testimonialsProgressFill');

  if (btnPrev && btnNext && reviewText && reviewName && reviewAvatar && counter && progressFill) {
    const reviews = [
      {
        text: '„Sehr schneller und professioneller Service. Preis wurde vorher klar kommuniziert. Kann Lukas nur weiterempfehlen!“',
        name: 'Michael S.',
        avatar: '/images/avatar-michael.jpg'
      },
      {
        text: '„Hat mir spät abends noch geholfen, als ich mich ausgesperrt hatte. Innerhalb kurzer Zeit vor Ort und die Tür ohne Schäden geöffnet. Sehr freundlich und kompetent.“',
        name: 'Sabine K.',
        avatar: '/images/avatar-sabine.jpg'
      },
      {
        text: '„Zuverlässig, pünktlich und fachlich top. Die Beratung zu neuen Schließzylindern war sehr hilfreich. Wir fühlen uns jetzt deutlich sicherer.“',
        name: 'Thomas R.',
        avatar: '/images/avatar-thomas.jpg'
      }
    ];

    let currentIndex = 0;

    const updateReview = (index) => {
      currentIndex = (index + reviews.length) % reviews.length;
      reviewText.style.opacity = '0';
      reviewText.style.transform = 'translateY(6px)';
      
      setTimeout(() => {
        reviewText.textContent = reviews[currentIndex].text;
        reviewName.textContent = reviews[currentIndex].name;
        reviewAvatar.src = reviews[currentIndex].avatar;
        reviewAvatar.alt = `Kunde ${reviews[currentIndex].name}`;
        counter.textContent = `0${currentIndex + 1} / 0${reviews.length}`;
        progressFill.style.width = `${((currentIndex + 1) / reviews.length) * 100}%`;
        
        reviewText.style.opacity = '1';
        reviewText.style.transform = 'translateY(0)';
      }, 180);
    };

    btnPrev.addEventListener('click', () => updateReview(currentIndex - 1));
    btnNext.addEventListener('click', () => updateReview(currentIndex + 1));
  }

  // Smooth scroll for footer back-to-top link
  const backToTopLinks = document.querySelectorAll('.footer-back-to-top');
  backToTopLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  });

  // ==========================================================================
  // EDITORIAL CONTACT FORM VALIDATION & SUBMISSION
  // ==========================================================================
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    const nameInput = document.getElementById('contactName');
    const emailInput = document.getElementById('contactEmail');
    const phoneInput = document.getElementById('contactPhone');
    const subjectSelect = document.getElementById('contactSubject');
    const messageTextarea = document.getElementById('contactMessage');
    const consentCheckbox = document.getElementById('contactConsent');
    const submitBtn = document.getElementById('btnSubmitContact');
    const statusMsg = document.getElementById('formStatusMsg');

    const nameError = document.getElementById('nameError');
    const emailError = document.getElementById('emailError');
    const subjectError = document.getElementById('subjectError');
    const messageError = document.getElementById('messageError');
    const consentError = document.getElementById('consentError');

    const clearErrors = () => {
      [nameInput, emailInput, phoneInput, subjectSelect, messageTextarea].forEach(el => {
        if (el) el.classList.remove('is-invalid');
      });
      [nameError, emailError, subjectError, messageError, consentError].forEach(err => {
        if (err) {
          err.textContent = '';
          err.classList.remove('is-visible');
        }
      });
      if (statusMsg) {
        statusMsg.style.display = 'none';
        statusMsg.className = 'form-status-msg';
        statusMsg.textContent = '';
      }
    };

    const validateEmail = (email) => {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    };

    // Real-time error clearance on input
    [nameInput, emailInput, phoneInput, messageTextarea].forEach(field => {
      if (field) {
        field.addEventListener('input', () => {
          field.classList.remove('is-invalid');
          const errorSpan = document.getElementById(field.id === 'contactName' ? 'nameError' : field.id === 'contactEmail' ? 'emailError' : 'messageError');
          if (errorSpan) {
            errorSpan.textContent = '';
            errorSpan.classList.remove('is-visible');
          }
        });
      }
    });

    if (subjectSelect) {
      subjectSelect.addEventListener('change', () => {
        subjectSelect.classList.remove('is-invalid');
        if (subjectError) {
          subjectError.textContent = '';
          subjectError.classList.remove('is-visible');
        }
      });
    }

    if (consentCheckbox) {
      consentCheckbox.addEventListener('change', () => {
        if (consentError) {
          consentError.textContent = '';
          consentError.classList.remove('is-visible');
        }
      });
    }

    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      clearErrors();

      let isValid = true;
      let firstInvalidField = null;

      // 1. Name validation
      if (!nameInput.value.trim()) {
        isValid = false;
        nameInput.classList.add('is-invalid');
        nameError.textContent = 'Bitte geben Sie Ihren Namen ein.';
        nameError.classList.add('is-visible');
        if (!firstInvalidField) firstInvalidField = nameInput;
      }

      // 2. Email validation
      const emailVal = emailInput.value.trim();
      if (!emailVal) {
        isValid = false;
        emailInput.classList.add('is-invalid');
        emailError.textContent = 'Bitte geben Sie Ihre E-Mail-Adresse ein.';
        emailError.classList.add('is-visible');
        if (!firstInvalidField) firstInvalidField = emailInput;
      } else if (!validateEmail(emailVal)) {
        isValid = false;
        emailInput.classList.add('is-invalid');
        emailError.textContent = 'Bitte geben Sie eine gültige E-Mail-Adresse ein.';
        emailError.classList.add('is-visible');
        if (!firstInvalidField) firstInvalidField = emailInput;
      }

      // 3. Subject validation
      if (!subjectSelect.value) {
        isValid = false;
        subjectSelect.classList.add('is-invalid');
        subjectError.textContent = 'Bitte wählen Sie Ihr Anliegen aus.';
        subjectError.classList.add('is-visible');
        if (!firstInvalidField) firstInvalidField = subjectSelect;
      }

      // 4. Message validation
      if (!messageTextarea.value.trim()) {
        isValid = false;
        messageTextarea.classList.add('is-invalid');
        messageError.textContent = 'Bitte geben Sie Ihre Nachricht ein.';
        messageError.classList.add('is-visible');
        if (!firstInvalidField) firstInvalidField = messageTextarea;
      }

      // 5. Consent validation
      if (!consentCheckbox.checked) {
        isValid = false;
        consentError.textContent = 'Bitte akzeptieren Sie die Datenschutzerklärung vor dem Absenden.';
        consentError.classList.add('is-visible');
        if (!firstInvalidField) firstInvalidField = consentCheckbox;
      }

      if (!isValid) {
        if (firstInvalidField) firstInvalidField.focus();
        return;
      }

      // Form submission feedback
      const labelSpan = submitBtn.querySelector('.submit-label');
      const arrowSpan = submitBtn.querySelector('.submit-arrow');
      const originalText = labelSpan ? labelSpan.textContent : 'ANFRAGE SENDEN';

      submitBtn.disabled = true;
      if (labelSpan) labelSpan.textContent = 'WIRD GESENDET...';
      if (arrowSpan) arrowSpan.style.display = 'none';

      // Simulating clean asynchronous transmission
      setTimeout(() => {
        contactForm.reset();
        submitBtn.disabled = false;
        if (labelSpan) labelSpan.textContent = 'ANFRAGE GESENDET ✓';
        if (arrowSpan) arrowSpan.style.display = 'inline-block';

        statusMsg.className = 'form-status-msg status-success';
        statusMsg.innerHTML = '<strong>Vielen Dank! Ihre Anfrage wurde erfolgreich übermittelt.</strong><br>Wir prüfen Ihr Anliegen und setzen uns schnellstmöglich mit Ihnen in Verbindung.';
        statusMsg.style.display = 'block';

        setTimeout(() => {
          if (labelSpan) labelSpan.textContent = originalText;
        }, 5000);
      }, 650);
    });
  }
});

// Production Content Protection & Inspection Deterrence
(() => {
  // Disable right-click context menu
  document.addEventListener('contextmenu', (e) => {
    e.preventDefault();
  }, false);

  // Disable DevTools shortcuts
  document.addEventListener('keydown', (e) => {
    // F12
    if (e.key === 'F12' || e.keyCode === 123) {
      e.preventDefault();
      return false;
    }
    // Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+Shift+C
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && ['I', 'i', 'J', 'j', 'C', 'c'].includes(e.key)) {
      e.preventDefault();
      return false;
    }
    // Ctrl+U (View Source)
    if ((e.ctrlKey || e.metaKey) && (e.key === 'u' || e.key === 'U')) {
      e.preventDefault();
      return false;
    }
    // Ctrl+S (Save Page)
    if ((e.ctrlKey || e.metaKey) && (e.key === 's' || e.key === 'S')) {
      e.preventDefault();
      return false;
    }
  }, false);

  // Periodic console clear & copyright note
  try {
    const showNotice = () => {
      console.clear();
      console.log(
        '%cSchlüsselnotdienst Rhein-Selz\n%cAlle Inhalte, Texte und Quellcodes sind urheberrechtlich geschützt.',
        'color:#e1252b;font-size:16px;font-weight:bold;font-family:sans-serif;',
        'color:#444;font-size:12px;font-family:sans-serif;'
      );
    };
    showNotice();
    setInterval(showNotice, 4000);
  } catch (_) {}
})();



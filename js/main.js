/* ========================================
   RUSHITI RENOVATION BESANCON - Main JS
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {

    // --- Navbar scroll effect ---
    const navbar = document.getElementById('navbar');
    const backToTop = document.getElementById('backToTop');

    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        navbar.classList.toggle('scrolled', scrollY > 50);
        backToTop.classList.toggle('visible', scrollY > 500);
    });

    // --- Mobile nav toggle ---
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navLinks.classList.toggle('active');
        document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
    });

    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.style.overflow = '';
        });
    });

    // --- Back to top ---
    backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // --- Stat counter animation ---
    const counters = document.querySelectorAll('.stat-number');
    let countersDone = false;

    function animateCounters() {
        if (countersDone) return;
        counters.forEach(counter => {
            const target = parseFloat(counter.getAttribute('data-target'));
            const decimals = Number.isInteger(target) ? 0 : 1;
            const format = value => value.toFixed(decimals).replace('.', ',');
            const duration = 2000;
            const step = target / (duration / 16);
            let current = 0;

            const update = () => {
                current += step;
                if (current >= target) {
                    counter.textContent = format(target);
                    return;
                }
                counter.textContent = format(current);
                requestAnimationFrame(update);
            };
            update();
        });
        countersDone = true;
    }

    // Observe hero stats for counter animation
    const statsSection = document.querySelector('.hero-stats');
    if (statsSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounters();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        observer.observe(statsSection);
    }

    // --- Gallery Filter ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.getAttribute('data-filter');

            galleryItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.classList.remove('hidden');
                    item.style.animation = 'fadeIn 0.4s ease forwards';
                } else {
                    item.classList.add('hidden');
                }
            });
        });
    });

    // --- Testimonial Slider ---
    const track = document.getElementById('testimonialTrack');
    const dotsContainer = document.getElementById('testimonialDots');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (track) {
        const cards = track.querySelectorAll('.testimonial-card');
        let currentIndex = 0;
        let slidesPerView = window.innerWidth >= 768 ? 2 : 1;
        const totalSlides = Math.ceil(cards.length / slidesPerView);

        function createDots() {
            dotsContainer.innerHTML = '';
            for (let i = 0; i < totalSlides; i++) {
                const dot = document.createElement('span');
                dot.className = 'dot' + (i === 0 ? ' active' : '');
                dot.addEventListener('click', () => goToSlide(i));
                dotsContainer.appendChild(dot);
            }
        }

        function goToSlide(index) {
            currentIndex = index;
            const offset = -(100 / slidesPerView) * currentIndex * slidesPerView;
            track.style.transform = `translateX(${offset}%)`;
            const dots = dotsContainer.querySelectorAll('.dot');
            dots.forEach((d, i) => d.classList.toggle('active', i === currentIndex));
        }

        prevBtn.addEventListener('click', () => {
            goToSlide(currentIndex > 0 ? currentIndex - 1 : totalSlides - 1);
        });

        nextBtn.addEventListener('click', () => {
            goToSlide(currentIndex < totalSlides - 1 ? currentIndex + 1 : 0);
        });

        // Auto slide
        let autoSlide = setInterval(() => {
            goToSlide(currentIndex < totalSlides - 1 ? currentIndex + 1 : 0);
        }, 5000);

        track.addEventListener('mouseenter', () => clearInterval(autoSlide));
        track.addEventListener('mouseleave', () => {
            autoSlide = setInterval(() => {
                goToSlide(currentIndex < totalSlides - 1 ? currentIndex + 1 : 0);
            }, 5000);
        });

        window.addEventListener('resize', () => {
            const newSlidesPerView = window.innerWidth >= 768 ? 2 : 1;
            if (newSlidesPerView !== slidesPerView) {
                slidesPerView = newSlidesPerView;
                currentIndex = 0;
                createDots();
                goToSlide(0);
            }
        });

        createDots();
    }

    // --- Contact Form (ouvre le client email avec la demande pre-remplie) ---
    const form = document.getElementById('contactForm');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            const data = new FormData(form);
            const serviceSelect = form.querySelector('#service');
            const serviceLabel = serviceSelect.options[serviceSelect.selectedIndex].text;

            const subject = 'Demande de devis' + (data.get('service') ? ' - ' + serviceLabel : '');
            const body = [
                'Nom : ' + data.get('nom'),
                'Prénom : ' + data.get('prenom'),
                'Email : ' + data.get('email'),
                'Téléphone : ' + data.get('telephone'),
                'Type de travaux : ' + (data.get('service') ? serviceLabel : 'Non précisé'),
                '',
                'Description du projet :',
                data.get('message')
            ].join('\n');

            window.location.href = 'mailto:contact@rushiti-renovation.fr'
                + '?subject=' + encodeURIComponent(subject)
                + '&body=' + encodeURIComponent(body);

            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.textContent;
            btn.textContent = 'Ouverture de votre messagerie...';
            btn.disabled = true;

            setTimeout(() => {
                btn.textContent = originalText;
                btn.disabled = false;
            }, 3000);
        });
    }

    // --- Smooth reveal on scroll ---
    const revealElements = document.querySelectorAll('.service-card, .step, .info-card, .gallery-item');

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });

    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        revealObserver.observe(el);
    });

    // --- Active nav link on scroll ---
    const sections = document.querySelectorAll('section[id]');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute('id');
            }
        });

        navLinks.querySelectorAll('a').forEach(link => {
            link.classList.remove('active-link');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active-link');
            }
        });
    });
});

// Fade in animation keyframe
const style = document.createElement('style');
style.textContent = `@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }`;
document.head.appendChild(style);

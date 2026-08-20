/* ========================================
   RUSHITI RENOVATION BESANCON - Main JS
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // --- Navbar & back-to-top on scroll (un seul écouteur, throttlé en rAF) ---
    const navbar = document.getElementById('navbar');
    const backToTop = document.getElementById('backToTop');
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');
    const sections = document.querySelectorAll('section[id]');

    let scrollQueued = false;

    function onScroll() {
        const scrollY = window.scrollY;

        if (navbar) navbar.classList.toggle('scrolled', scrollY > 50);
        if (backToTop) backToTop.classList.toggle('visible', scrollY > 500);

        // Lien de navigation actif
        if (navLinks) {
            let current = '';
            sections.forEach(section => {
                if (scrollY >= section.offsetTop - 120) {
                    current = section.getAttribute('id');
                }
            });
            navLinks.querySelectorAll('a').forEach(link => {
                link.classList.toggle('active-link', link.getAttribute('href') === '#' + current);
            });
        }

        scrollQueued = false;
    }

    window.addEventListener('scroll', () => {
        if (scrollQueued) return;
        scrollQueued = true;
        requestAnimationFrame(onScroll);
    }, { passive: true });

    onScroll();

    // --- Mobile nav toggle ---
    if (navToggle && navLinks) {
        const setNav = (open) => {
            navToggle.classList.toggle('active', open);
            navLinks.classList.toggle('active', open);
            navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            navToggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
            document.body.style.overflow = open ? 'hidden' : '';
        };

        navToggle.addEventListener('click', () => {
            setNav(!navLinks.classList.contains('active'));
        });

        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => setNav(false));
        });

        // Échap ferme le menu et rend le focus au bouton.
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navLinks.classList.contains('active')) {
                setNav(false);
                navToggle.focus();
            }
        });
    }

    // --- Back to top ---
    if (backToTop) {
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
        });
    }

    // --- Compteur du hero ---
    // Uniquement les éléments portant un data-target numérique : sans ce filtre,
    // parseInt(null) donne NaN et la boucle d'animation ne se termine jamais.
    const counters = Array.from(document.querySelectorAll('.stat-number'))
        .map(el => ({ el, target: parseInt(el.getAttribute('data-target'), 10) }))
        .filter(c => Number.isFinite(c.target));

    function animateCounters() {
        counters.forEach(({ el, target }) => {
            if (reduceMotion) {
                el.textContent = target;
                return;
            }

            const duration = 2000;
            const step = target / (duration / 16);
            let current = 0;

            const update = () => {
                current += step;
                if (current >= target) {
                    el.textContent = target;
                    return;
                }
                el.textContent = Math.floor(current);
                requestAnimationFrame(update);
            };
            update();
        });
    }

    const statsSection = document.querySelector('.hero-stats');
    if (statsSection && counters.length) {
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

    // --- Filtre de la galerie ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => {
                b.classList.remove('active');
                b.setAttribute('aria-pressed', 'false');
            });
            btn.classList.add('active');
            btn.setAttribute('aria-pressed', 'true');

            const filter = btn.getAttribute('data-filter');

            galleryItems.forEach(item => {
                const shown = filter === 'all' || item.getAttribute('data-category') === filter;
                item.classList.toggle('hidden', !shown);
                // Masqué visuellement ET retiré de l'ordre de tabulation et des
                // lecteurs d'écran, sinon le contenu filtré reste atteignable.
                item.hidden = !shown;
                if (shown && !reduceMotion) {
                    item.style.animation = 'fadeIn 0.4s ease forwards';
                }
            });
        });
    });

    // --- Formulaire de contact (ouvre le client email avec la demande pré-remplie) ---
    const form = document.getElementById('contactForm');
    const formStatus = document.getElementById('formStatus');

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
                // Aucun retour n'est possible depuis un lien mailto : on affiche
                // systématiquement l'adresse pour les visiteurs sans client mail.
                if (formStatus) {
                    formStatus.textContent = 'Votre messagerie devrait s’ouvrir avec la demande pré-remplie. '
                        + 'Si ce n’est pas le cas, écrivez-nous à contact@rushiti-renovation.fr '
                        + 'ou appelez le 07 60 27 98 97.';
                }
            }, 3000);
        });
    }

    // --- Apparition au défilement ---
    const revealElements = document.querySelectorAll('.service-card, .step, .info-card, .gallery-item, .engagement-card');

    if (!reduceMotion) {
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
    }
});

// Fade in animation keyframe
const style = document.createElement('style');
style.textContent = `@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }`;
document.head.appendChild(style);

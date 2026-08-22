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
            const target = parseInt(counter.getAttribute('data-target'));
            const duration = 2000;
            const step = target / (duration / 16);
            let current = 0;

            const update = () => {
                current += step;
                if (current >= target) {
                    counter.textContent = target;
                    return;
                }
                counter.textContent = Math.floor(current);
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

    // --- Carrousel Avis Google ---
    // La piste est un conteneur scroll-snap : le glissement tactile et le clavier
    // fonctionnent nativement, y compris si ce script ne se charge pas. Le JS
    // n'ajoute que les flèches, les puces, le défilement auto et le « lire la suite ».
    const piste = document.getElementById('avisPiste');

    if (piste) {
        const carrousel = piste.closest('.avis-carrousel');
        const cartes = Array.from(piste.querySelectorAll('.avis-card'));
        const dotsAvis = document.getElementById('avisDots');
        const avisPrev = document.getElementById('avisPrev');
        const avisNext = document.getElementById('avisNext');
        const DELAI_AUTO = 6000;
        let defilement = null;
        // Page visée, et non page lue dans le DOM : pendant un défilement animé,
        // scrollLeft est encore à mi-course et deux clics rapprochés se marchent dessus.
        let pageVisee = 0;

        carrousel.classList.add('js-avis');

        // Nombre de cartes entièrement visibles — mesuré, jamais déduit d'un breakpoint
        function parVue() {
            const origine = cartes[0].offsetLeft;
            const largeur = piste.clientWidth;
            const visibles = cartes.filter(c => c.offsetLeft - origine < largeur - 1).length;
            return Math.max(1, visibles);
        }

        function nbPages() {
            return Math.ceil(cartes.length / parVue());
        }

        function pageActuelle() {
            const origine = cartes[0].offsetLeft;
            const x = piste.scrollLeft;
            let index = 0;
            cartes.forEach((c, i) => {
                if (c.offsetLeft - origine <= x + 2) index = i;
            });
            return Math.min(Math.round(index / parVue()), nbPages() - 1);
        }

        function allerPage(page) {
            const n = parVue();
            pageVisee = page;
            const cible = cartes[Math.min(page * n, cartes.length - 1)];
            piste.scrollTo({ left: cible.offsetLeft - cartes[0].offsetLeft });
            majPuces();
        }

        function majPuces() {
            dotsAvis.querySelectorAll('.dot').forEach((d, i) => {
                d.classList.toggle('active', i === pageVisee);
                d.setAttribute('aria-current', i === pageVisee ? 'true' : 'false');
            });
        }

        function creerPuces() {
            dotsAvis.innerHTML = '';
            const total = nbPages();
            if (total < 2) return;
            for (let i = 0; i < total; i++) {
                const puce = document.createElement('button');
                puce.type = 'button';
                puce.className = 'dot';
                puce.setAttribute('aria-label', 'Avis ' + (i + 1) + ' sur ' + total);
                puce.addEventListener('click', () => {
                    allerPage(i);
                    relancerAuto();
                });
                dotsAvis.appendChild(puce);
            }
            majPuces();
        }

        function decaler(sens) {
            const total = nbPages();
            allerPage((pageVisee + sens + total) % total);
        }

        // Défilement automatique — suspendu au survol, au focus clavier,
        // quand l'onglet passe en arrière-plan, et jamais lancé si l'utilisateur
        // a demandé moins d'animations.
        const moinsAnimations = window.matchMedia('(prefers-reduced-motion: reduce)');

        // Rien ne tourne tant que la section n'est pas à l'écran : inutile de faire
        // défiler des avis que personne ne regarde, et le visiteur qui arrive dessus
        // la trouve au premier avis plutôt qu'au milieu.
        let sectionVisible = false;

        function stopperAuto() {
            clearInterval(defilement);
            defilement = null;
        }

        function lancerAuto() {
            if (defilement || !sectionVisible || moinsAnimations.matches || nbPages() < 2) return;
            defilement = setInterval(() => decaler(1), DELAI_AUTO);
        }

        function relancerAuto() {
            stopperAuto();
            lancerAuto();
        }

        avisPrev.addEventListener('click', () => { decaler(-1); relancerAuto(); });
        avisNext.addEventListener('click', () => { decaler(1); relancerAuto(); });

        piste.addEventListener('mouseenter', stopperAuto);
        piste.addEventListener('mouseleave', lancerAuto);
        piste.addEventListener('focusin', stopperAuto);
        piste.addEventListener('focusout', lancerAuto);
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) stopperAuto(); else lancerAuto();
        });

        let tempoScroll;
        piste.addEventListener('scroll', () => {
            clearTimeout(tempoScroll);
            tempoScroll = setTimeout(() => {
                pageVisee = pageActuelle();
                majPuces();
            }, 120);
        });

        let largeurConnue = piste.clientWidth;
        window.addEventListener('resize', () => {
            if (piste.clientWidth === largeurConnue) return;
            largeurConnue = piste.clientWidth;
            // Le nombre de pages change avec la largeur : on repart de la première.
            pageVisee = 0;
            creerPuces();
            allerPage(0);
        });

        // « Lire l'avis complet » : n'apparaît que sur les avis réellement tronqués.
        cartes.forEach(carte => {
            const texte = carte.querySelector('.avis-texte');
            texte.classList.add('is-clampe');
            if (texte.scrollHeight <= texte.clientHeight + 2) return;

            const bouton = document.createElement('button');
            bouton.type = 'button';
            bouton.className = 'avis-plus';
            bouton.textContent = 'Lire l’avis complet';
            bouton.setAttribute('aria-expanded', 'false');
            bouton.addEventListener('click', () => {
                const ouvert = texte.classList.toggle('is-clampe') === false;
                bouton.setAttribute('aria-expanded', String(ouvert));
                bouton.textContent = ouvert ? 'Réduire' : 'Lire l’avis complet';
            });
            carte.appendChild(bouton);
        });

        new IntersectionObserver(entrees => {
            entrees.forEach(entree => {
                sectionVisible = entree.isIntersecting;
                if (sectionVisible) lancerAuto(); else stopperAuto();
            });
        }, { threshold: 0.25 }).observe(piste);

        creerPuces();
    }

    // --- Contact Form (envoi direct via Web3Forms — action/method portés par le <form>,
    //     même compte que rushiti-renovation.fr ; redirection vers /merci après envoi) ---
    const form = document.getElementById('contactForm');
    if (form) {
        const status = form.querySelector('.form-status');

        form.addEventListener('submit', (e) => {
            // Champs pièges anti-spam : remplis/cochés = robot, on n'envoie pas
            const piege = form.querySelector('input[name="entreprise_hp"]');
            const robot = form.querySelector('input[name="botcheck"]');
            if ((piege && piege.value) || (robot && robot.checked)) {
                e.preventDefault();
                return;
            }

            const btn = form.querySelector('button[type="submit"]');
            btn.disabled = true;
            btn.textContent = 'Envoi en cours\u2026';
            if (status) {
                status.textContent = 'Envoi de votre demande\u2026';
            }
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

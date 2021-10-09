<template>
  <div id="app" class="flex flex-col min-h-screen page__disclaimer">
    <div class="app-header-mobile u-no-print">
      <!---->
      <header class="app-header-mobile__outer">
        <div class="app-header-mobile__inner">
          <button class="c-hamburger">
            <span class="c-hamburger__icon"></span
            ><span class="sr-only">Open Menu</span></button
          ><img
            src="/img/_logo-usps-eagle-only.f7be4b59.svg"
            alt="The profile of an eagle's head."
            class="app-header-mobile__logo"
          />
        </div>
      </header>
    </div>
    <div class="flex-grow">
      <div>
        <!----><!---->
        <main id="main" class="bg-white" style="">
          <header id="hero" class="bg-blue-200">
            <div class="px-6 py-8">
              <h1 class="text-white mb-4">
                Official USPS<sup>®</sup><br />Change-of-Address
              </h1>
              <p class="text-white mb-4">
                By clicking Get Started, I understand and acknowledge the
                statements below.
              </p>
              <a
                href="/mgo/move-combined"
                class="c-btn--ghost"
                id="get-started-top"
              >
                Get Started
              </a>
            </div>
          </header>
          <div id="exp-value-props"></div>
          <section class="p-6">
            <p class="mb-4">
              <strong>Note:</strong> The person who prepares this form states
              that he or she is the person, executor, guardian, authorized
              officer, or agent of the person for whom mail would be forwarded
              under this order. Anyone submitting false or inaccurate
              information on this form is subject to punishment by fine or
              imprisonment or both under Sections 2, 1001, 1702 and 1708 of
              Title 18, United States Code.
            </p>
            <a
              href="https://about.usps.com/who/legal/privacy-policy/full-privacy-policy.htm"
              target="_blank"
              rel="noopener noreferrer"
              class="c-link--inline pr-4"
              >Privacy Policy</a
            ><a href="/mgo/terms-of-use" class="c-link--inline" target="_blank"
              ><span>Terms of Use</span></a
            >
            <p class="mt-4">
              <strong>Note:</strong> To complete the Online Change-of-Address
              you will need a valid email address as well as a valid credit or
              debit card for the $1.10 charge.
            </p>
          </section>
          <div class="w-screen bg-blue-200">
            <div class="flex items-center u-container--x py-6">
              <div class="mr-2 text-xl text-white">
                Want to
                <a
                  id="view-edit-coac"
                  href="https://coacdev01.imagitas.com"
                  title="Official USPS Change of Address Correct Form"
                  class="font-bold"
                >
                  View, Edit, Cancel
                </a>
                or
                <a
                  id="disputes-home"
                  href="https://coacdev01.imagitas.com/mgoc/disputes"
                  title="Official USPS Change of Address Disputes Form"
                  class="font-bold"
                >
                  Dispute
                </a>
                a Change-of-Address?
              </div>
              <div class="w-4 not-sr-only">
                <a
                  href="https://coacdev01.imagitas.com"
                  title="Official USPS Change of Address Correct Form"
                  ><span class="red-arrow"></span
                ></a>
              </div>
            </div>
          </div>
          <div class="mt-10">
            <p class="disclaimer-mobile__get-started-text">
              By clicking Get Started, I understand and acknowledge the
              statements below.
            </p>
            <a
              href="/mgo/move-combined"
              class="c-btn w-full rounded-none"
              id="get-started-body"
            >
              Get Started
            </a>
          </div>
        </main>
      </div>
    </div>
    <!---->
    <footer class="app-footer u-no-print">
      <div class="app-footer__content">
        <a
          href="https://www.usps.com/"
          rel="noopener noreferrer"
          target="_blank"
          class="app-footer__logo-link"
          ><img
            src="/img/_logo-usps.fde3b51c.svg"
            alt="The profile of an eagle's head adjoining the words USPS.com."
            class="app-footer__logo"
        /></a>
        <div class="app-footer__nav-links mt-6">
          <div class="app-footer__nav-group">
            <p class="app-footer__nav-heading">Helpful Links</p>
            <ul class="mt-1">
              <li>
                <a
                  href="https://www.usps.com/help/welcome.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Contact Us</a
                >
              </li>
              <li>
                <a
                  href="https://www.usps.com/globals/site-index.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Site Index</a
                >
              </li>
              <li>
                <a
                  href="http://faq.usps.com/"
                  rel="noopener noreferrer"
                  target="_blank"
                  >FAQs</a
                >
              </li>
              <li>
                <a
                  id="footer-mail-forwarding-instructions"
                  href="https://mgodev01.imagitas.com/mgo/mail-forwarding-instructions"
                  target="_blank"
                >
                  Mail Forwarding Instructions
                </a>
              </li>
              <li>
                <a
                  id="footer-temporary-moves"
                  href="https://mgodev01.imagitas.com/mgo/temporary-moves"
                  target="_blank"
                >
                  Temporary Moves
                </a>
              </li>
              <li>
                <a
                  id="footer-when-to-file"
                  href="https://mgodev01.imagitas.com/mgo/when-to-file"
                  target="_blank"
                >
                  When to File
                </a>
              </li>
              <li>
                <a
                  id="footer-types-of-forwarding"
                  href="https://mgodev01.imagitas.com/mgo/types-of-forwarding"
                  target="_blank"
                >
                  Types of Forwarding
                </a>
              </li>
            </ul>
          </div>
          <div class="app-footer__nav-group">
            <p class="app-footer__nav-heading">USPS Jobs</p>
            <ul class="mt-1">
              <li>
                <a
                  href="http://about.usps.com/careers/welcome.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Careers</a
                >
              </li>
            </ul>
            <p class="app-footer__nav-heading mt-3">On about.usps.com</p>
            <ul class="mt-1">
              <li>
                <a
                  href="http://about.usps.com/"
                  rel="noopener noreferrer"
                  target="_blank"
                  >About USPS Home</a
                >
              </li>
              <li>
                <a
                  href="http://about.usps.com/news/welcome.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Newsroom</a
                >
              </li>
              <li>
                <a
                  href="http://about.usps.com/news/service-alerts/welcome.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >USPS Service Updates</a
                >
              </li>
              <li>
                <a
                  href="http://about.usps.com/forms-publications/welcome.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Forms &amp; Publications</a
                >
              </li>
              <li>
                <a
                  href="https://www.usps.com/gov-services/gov-services.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Government Services</a
                >
              </li>
            </ul>
          </div>
          <div class="app-footer__nav-group">
            <p class="app-footer__nav-heading">Other USPS Sites</p>
            <ul class="mt-1">
              <li>
                <a
                  href="https://gateway.usps.com/"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Business Customer Gateway</a
                >
              </li>
              <li>
                <a
                  href="https://postalinspectors.uspis.gov/"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Postal Inspectors</a
                >
              </li>
              <li>
                <a
                  href="http://www.uspsoig.gov/"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Inspector General</a
                >
              </li>
              <li>
                <a
                  href="http://pe.usps.gov/"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Postal Explorer</a
                >
              </li>
              <li>
                <a
                  href="http://www.postalmuseum.si.edu/"
                  rel="noopener noreferrer"
                  target="_blank"
                  >National Postal Museum</a
                >
              </li>
              <li>
                <a
                  href="https://www.usps.com/webtools/welcome.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Resources for Developers</a
                >
              </li>
              <li>
                <a
                  href="https://postalpro.usps.com/"
                  rel="noopener noreferrer"
                  target="_blank"
                  >PostalPro</a
                >
              </li>
            </ul>
          </div>
          <div class="app-footer__nav-group">
            <p class="app-footer__nav-heading">Legal Information</p>
            <ul class="mt-1">
              <li>
                <a
                  href="https://about.usps.com/who/legal/privacy-policy/full-privacy-policy.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Privacy Policy</a
                >
              </li>
              <li>
                <a
                  href="http://about.usps.com/termsofuse.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >Terms of Use</a
                >
              </li>
              <li>
                <a
                  href="http://about.usps.com/who-we-are/foia/welcome.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >FOIA</a
                >
              </li>
              <li>
                <a
                  href="http://about.usps.com/who-we-are/no-fear-act/welcome.htm"
                  rel="noopener noreferrer"
                  target="_blank"
                  >No FEAR Act EEO Data</a
                >
              </li>
            </ul>
          </div>
        </div>
        <p class="text-sm mt-6">Copyright © 2021 USPS. All Rights Reserved.</p>
        <div class="c-hairline mt-6"></div>
        <ul class="app-footer__social">
          <li>
            <a
              href="http://www.facebook.com/usps"
              rel="noopener noreferrer"
              target="_blank"
              ><img
                src="/img/_logo-facebook.8fe8e02a.svg"
                alt="USPS Facebook link"
                class="app-footer__social-icon"
            /></a>
          </li>
          <li class="ml-4">
            <a
              href="http://twitter.com/usps"
              rel="noopener noreferrer"
              target="_blank"
              ><img
                src="/img/_logo-twitter.3a33930e.svg"
                alt="USPS Twitter link"
                class="app-footer__social-icon"
            /></a>
          </li>
          <li class="ml-4">
            <a
              href="http://pinterest.com/uspsstamps"
              rel="noopener noreferrer"
              target="_blank"
              ><img
                src="/img/_logo-pinterest.6b399f57.svg"
                alt="USPS Pinterest link"
                class="app-footer__social-icon"
            /></a>
          </li>
          <li class="ml-4">
            <a
              href="http://www.youtube.com/usps"
              rel="noopener noreferrer"
              target="_blank"
              ><img
                src="/img/_logo-youtube.0cee7de3.svg"
                alt="USPS Youtube icon link"
                class="app-footer__social-icon"
            /></a>
          </li>
        </ul>
      </div>
    </footer>
    <!---->
  </div>
</template>

<script>
export default {
  name: "Postal",
};
</script>

<style scoped>
.resize-observer[data-v-b329ee4c] {
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  width: 100%;
  height: 100%;
  border: none;
  background-color: transparent;
  pointer-events: none;
  display: block;
  overflow: hidden;
  opacity: 0;
}
.resize-observer[data-v-b329ee4c] object {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: -1;
}

.c-accordion {
  font-size: 14px;
}
.c-accordion__summary {
  margin-bottom: 10px;
  font-size: 18px;
  font-weight: 700;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  list-style-type: none;
  cursor: pointer;
  border-radius: 2px;
}
.c-accordion__summary:focus {
  box-shadow: 0 0 0 2px #228bec;
}
.c-accordion__summary-content {
  display: flex;
  justify-content: space-between;
}
.c-accordion__icon {
  display: block;
  margin-right: 10px;
  width: 18px;
  height: 18px;
  border: 4px solid #333366;
  border-bottom-right-radius: 2px;
  border-right: 0px;
  border-top: 0px;
  border-top-left-radius: 2px;
}
.c-accordion__icon--closed {
  margin-bottom: 5px;
  transform: rotate(-45deg);
}
.c-accordion__icon--open {
  margin-top: 5px;
  transform: rotate(135deg);
}

/* the custom arrow css icon makes this focus look bad */

.c-accordion__summary:focus {
  outline: none;
}

/* remove the default arrow */

.c-accordion summary::-webkit-details-marker {
  display: none;
}

.app-loader {
  display: flex;
  justify-content: center;
  text-align: center;
}
.app-loader__container {
  width: 100%;
}
@media (min-width: 1024px) {
  .app-loader__container {
    width: 20%;
  }
}
.app-loader__message {
  font-size: 22px;
}

.app-footer {
  padding: 30px;
  --bg-opacity: 1;
  background-color: #f7f7f7;
  background-color: rgba(247, 247, 247, var(--bg-opacity));
  width: 100%;
  border-top-width: 1px;
  border-style: solid;
  --border-opacity: 1;
  border-color: #d8d8d8;
  border-color: rgba(216, 216, 216, var(--border-opacity));
  padding-bottom: 100px;
}
@media (min-width: 1024px) {
  .app-footer {
    padding-left: 100px;

    padding-right: 100px;

    padding-bottom: 30px;
  }
}

@media (min-width: 1024px) {
  .app-footer__content {
    max-width: 1180px;

    margin-left: auto;

    margin-right: auto;
  }
}

.app-footer__logo {
  height: 16px;
}

.app-footer__nav-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 30px;
  font-size: 12px;
  font-weight: 500;
  --text-opacity: 1;
  color: #000;
  color: rgba(0, 0, 0, var(--text-opacity));
  line-height: 1.25rem;
}

@media (min-width: 1024px) {
  .app-footer__nav-links {
    flex-wrap: nowrap;
  }
}

.app-footer__nav-links a:hover {
  --text-opacity: 1;
  color: #3573b1;
  color: rgba(53, 115, 177, var(--text-opacity));
}

.app-footer__nav-group {
  width: calc(50% - 20px);
}

/* Mobile two column layout */

.app-footer__nav-group:nth-of-type(2) {
  order: 2;
}

.app-footer__nav-group:nth-of-type(4) {
  order: 4;
}

.app-footer__nav-group:nth-of-type(even) {
  margin-top: 15px;
}

@media (min-width: 1024px) {
  .app-footer__nav-group {
    /* Desktop four column layout */

    width: 100%;
  }

  .app-footer__nav-group:nth-of-type(2),
  .app-footer__nav-group:nth-of-type(4) {
    order: 0;
  }

  .app-footer__nav-group:nth-of-type(even) {
    margin-top: 0px;
  }
}

.app-footer__nav-heading {
  font-size: 12px;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  text-transform: uppercase;
}

.app-footer__social {
  display: flex;
  align-items: center;
  padding-top: 20px;
}

.app-footer__social-icon {
  width: 40px;
}

.app-header-desktop {
  --bg-opacity: 1;
  background-color: #f7f7f7;
  background-color: rgba(247, 247, 247, var(--bg-opacity));
  width: 100%;
  padding-left: 100px;
  padding-right: 100px;
  padding-top: 35px;
  padding-bottom: 35px;
  height: 95px;
}

.app-header-desktop__content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1180px;
  margin-left: auto;
  margin-right: auto;
}

.app-header-desktop__logo-link {
  flex: 1 1 auto;
}

.app-header-desktop__logo {
  height: 25px;
}

.app-header-desktop__nav-list {
  display: flex;
  align-items: center;
  font-weight: 700;
  font-size: 14px;
  --text-opacity: 1;
  color: #000;
  color: rgba(0, 0, 0, var(--text-opacity));
}

.app-header-desktop__nav-item {
  margin-right: 10px;
}

.app-header-desktop__nav-item:last-of-type {
  margin-right: 0px;
}

.app-header-desktop__nav-item--with-icon {
  display: flex;
  align-items: center;
}

.app-header-desktop__nav-item--divided-right {
  padding-right: 10px;
  border-right: 1px solid #000;
}

.app-header-desktop__icon-lock {
  display: inline-block;
  margin-right: 5px;
  width: 16px;
  height: 21px;
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAgCAMAAAA2a+hwAAAARVBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADc6ur3AAAAFnRSTlMAgIfy5gaTTxnDtGMX2NTOn3w5AUNCX5bWOwAAAJ9JREFUKM+1kVsSgyAMRSE8gvjWlv0vtUOmUlIl44/ni8sZ4AKqsOMyGjMuuKsT25y+zNu/61NFzx0mBtZuMFyaoZKepiYMASca+p9ztDA6Gkda6op8la3KEW9eNR4p8sJrjnAkyGktUueoeXpSOrDpEguOujUAZdvSqiRwX/oQfEt2uX3XkEAv25B0cS1KcVux0P2rCIhSfHjxy8TP/gBpKTMMfdyxVwAAAABJRU5ErkJggg==);
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
}

.app-header-mobile .c-hamburger {
  position: absolute;
  left: 0;
}

.app-header-mobile__outer {
  width: 100vw;
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 10px;
  padding-bottom: 10px;
  background-image: linear-gradient(to bottom, var(--gradient-color-stops));
  --gradient-from-color: #fff;
  --gradient-color-stops: var(--gradient-from-color),
    var(--gradient-to-color, rgba(255, 255, 255, 0));
  --gradient-to-color: #f7f7f7;
}

.app-header-mobile__inner {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.app-header-mobile__logo {
  height: auto;
  width: 60px;
}

.app-header-mobile__links {
  padding-left: 20px;
  padding-right: 20px;
  border-style: solid;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
  border-bottom-width: 1px;
  font-size: 14px;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.app-header-mobile__link-item {
  border-style: solid;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
  border-bottom-width: 1px;
}

.app-header-mobile__link-item:last-of-type {
  border-bottom-width: 0;
}

.app-header-mobile__link-item:last-of-type {
  border-bottom-width: 0;
}

.app-header-mobile__link {
  display: flex;
  align-items: center;
  padding-top: 10px;
  padding-bottom: 10px;
}

.app-header-mobile__icon {
  margin-right: 5px;
  position: static;
  width: auto;
  height: auto;
  padding: 0;
  margin: 0;
  overflow: visible;
  clip: auto;
  white-space: normal;
  width: 30px;
}

.app-header-mobile__legal-links {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 15px;
  font-size: 12px;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.app-header-mobile__legal-item:nth-of-type(2) .app-mobile-header__legal-link {
  border-right-width: 0;
}

.app-header-mobile__legal-link {
  margin-right: 10px;
  padding-right: 10px;
  border-style: solid;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
  border-right-width: 1px;
  font-weight: 700;
}

.app-header-mobile--slide-right {
  overflow: hidden;
}

.app-header-mobile--slide-right .app-header-mobile__outer {
  position: relative;
  padding-left: 10px;
  padding-right: 10px;
  z-index: 10;
  margin-left: calc(100vw - 45px);
}

.c-banner {
  --bg-opacity: 1;
  background-color: #f7f7f7;
  background-color: rgba(247, 247, 247, var(--bg-opacity));
}
.c-banner__container {
  width: 100%;
  max-width: 1180px;
  padding: 20px;
  font-size: 12px;
}
@media (min-width: 1024px) {
  .c-banner__container {
    padding-top: 30px;

    padding-bottom: 30px;

    padding-left: 40px;

    padding-right: 40px;

    font-size: 16px;
  }
}
.c-banner__heading {
  font-weight: 700;
}
.c-banner__message {
  margin-top: 10px;
}

/*
 * Modifiers - Look at seeing if we can align
 * the base styles with the default container widths
 */

.c-banner--alert {
  --bg-opacity: 1;
  background-color: #e71921;
  background-color: rgba(231, 25, 33, var(--bg-opacity));
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
}

.c-banner--alert .c-banner__container {
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
  padding-right: 20px;
}

@media (min-width: 1024px) {
  .c-banner--alert .c-banner__container {
    width: 100%;

    padding-left: 100px;

    padding-right: 100px;
  }
}

@media (min-width: 1380px) {
  .c-banner--alert .c-banner__container {
    max-width: 1180px;

    margin-left: auto;

    margin-right: auto;

    padding-left: 0px;

    padding-right: 0px;
  }
}

/* https://www.usps.com/styleguide/elements/buttons-links.htm */

.c-btn {
  padding-left: 20px;
  padding-right: 20px;
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
  font-size: 16px;
  font-weight: 700;
  display: inline-flex;
  align-content: center;
  justify-content: center;
  align-items: center;
  height: 44px;
  min-width: 170px;
  border-radius: 3px;
}

.c-btn:hover {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.c-btn--secondary {
  padding-left: 20px;
  padding-right: 20px;
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
  font-size: 16px;
  font-weight: 700;
  display: inline-flex;
  align-content: center;
  justify-content: center;
  align-items: center;
  height: 44px;
  min-width: 170px;
  border-radius: 3px;
}

.c-btn--secondary:hover {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.c-btn--secondary {
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
  border-width: 1px;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.c-btn--ghost {
  padding-left: 20px;
  padding-right: 20px;
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
  font-size: 16px;
  font-weight: 700;
  display: inline-flex;
  align-content: center;
  justify-content: center;
  align-items: center;
  height: 44px;
  min-width: 170px;
  border-radius: 3px;
}

.c-btn--ghost:hover {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.c-btn--ghost {
  background-color: transparent;
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
  border-width: 1px;
}

.c-btn--ghost-blue {
  padding-left: 20px;
  padding-right: 20px;
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
  font-size: 16px;
  font-weight: 700;
  display: inline-flex;
  align-content: center;
  justify-content: center;
  align-items: center;
  height: 44px;
  min-width: 170px;
  border-radius: 3px;
}

.c-btn--ghost-blue:hover {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.c-btn--ghost-blue {
  background-color: transparent;
  border-width: 1px;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.c-btn--disabled {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
  border-style: none;
  cursor: not-allowed;
}

.c-btn--disabled:hover {
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
}

.c-coa-item__label {
  font-size: 12px;
  --text-opacity: 1;
  color: #000;
  color: rgba(0, 0, 0, var(--text-opacity));
}
.c-coa-item__content {
  font-size: 14px;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  text-transform: uppercase;
}
@media (min-width: 1024px) {
  .c-coa-item__content {
    margin-top: 5px;

    font-size: 16px;
  }
}

.c-drawer {
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh;
}
.c-drawer__content {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  --bg-opacity: 1;
  background-color: #f7f7f7;
  background-color: rgba(247, 247, 247, var(--bg-opacity));
  z-index: 10;
  width: calc(100vw - 45px);
}
.c-drawer__backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
  background-color: rgba(0, 0, 0, 0.3);
}

.c-error-alert {
  display: flex;
}
.c-error-alert__icon {
  width: 20px;
  height: 100%;
  margin-right: 5px;
  margin-top: 1px;
}
@media (min-width: 1024px) {
  .c-error-alert__icon {
    margin-right: 10px;

    margin-top: 3px;
  }
}
.c-error-alert__message {
  font-size: 12px;
  font-weight: 700;
  --text-opacity: 1;
  color: #e71921;
  color: rgba(231, 25, 33, var(--text-opacity));
  max-width: calc(100% - 25px);
}
@media (min-width: 1024px) {
  .c-error-alert__message {
    font-size: 14px;

    max-width: calc(100% - 30px);
  }
}

.c-hairline {
  width: 100%;
  display: block;
  --bg-opacity: 1;
  background-color: #999;
  background-color: rgba(153, 153, 153, var(--bg-opacity));
  height: 1px;
}

.c-hamburger {
  position: relative;
  width: 25px;
  cursor: pointer;
  height: 21px;
}
.c-hamburger__icon {
  position: absolute;
  left: 0;
  width: 25px;
  height: 5px;
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
  top: 50%;
  margin-top: -2.5px;
  transition-duration: 80ms;
  transition-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
}
.c-hamburger__icon::before,
.c-hamburger__icon::after {
  position: absolute;
  display: block;
  width: 100%;
  height: 5px;
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
  content: "";
}
.c-hamburger__icon::before {
  top: -8px;
  transition: top 80ms 120ms ease;
}
.c-hamburger__icon::after {
  bottom: -8px;
  transition: bottom 80ms 120ms ease,
    transform 80ms cubic-bezier(0.55, 0.055, 0.675, 0.19);
}

.c-hamburger--active .c-hamburger__icon {
  --transform-translate-x: 0;
  --transform-translate-y: 0;
  --transform-rotate: 0;
  --transform-skew-x: 0;
  --transform-skew-y: 0;
  --transform-scale-x: 1;
  --transform-scale-y: 1;
  transform: translateX(var(--transform-translate-x))
    translateY(var(--transform-translate-y)) rotate(var(--transform-rotate))
    skewX(var(--transform-skew-x)) skewY(var(--transform-skew-y))
    scaleX(var(--transform-scale-x)) scaleY(var(--transform-scale-y));
  --transform-rotate: -45deg;
  transition: transform 80ms 120ms cubic-bezier(0.215, 0.61, 0.355, 1);
}

.c-hamburger--active .c-hamburger__icon::before {
  opacity: 0;
  top: 50%;
  transition: top 80ms ease, opacity 80ms 120ms ease;
}

.c-hamburger--active .c-hamburger__icon::after {
  bottom: 0;
  --transform-translate-x: 0;
  --transform-translate-y: 0;
  --transform-rotate: 0;
  --transform-skew-x: 0;
  --transform-skew-y: 0;
  --transform-scale-x: 1;
  --transform-scale-y: 1;
  transform: translateX(var(--transform-translate-x))
    translateY(var(--transform-translate-y)) rotate(var(--transform-rotate))
    skewX(var(--transform-skew-x)) skewY(var(--transform-skew-y))
    scaleX(var(--transform-scale-x)) scaleY(var(--transform-scale-y));
  --transform-rotate: -90deg;
  transition: bottom 80ms ease,
    transform 80ms 120ms cubic-bezier(0.215, 0.61, 0.355, 1);
}

.c-input-checkbox__label {
  position: relative;
  display: block;
  padding: 5px 10px 5px 25px;
  cursor: pointer;
}
.c-input-checkbox__label:before {
  content: "";
  position: absolute;
  left: 0;
  top: 7px;
  height: 14px;
  width: 14px;
  border: 1px solid #595959;
  border-radius: 3px;
}
input:focus + .c-input-checkbox__label:before {
  box-shadow: 0 0 0 2px #228bec;
}
input + .c-input-checkbox__label:after {
  content: "\2714";
  position: absolute;
  left: 2px;
  top: 4px;
  height: 8px;
  width: 8px;
  opacity: 0;
  transition: all 200ms ease-in;
}
input:checked + .c-input-checkbox__label:after {
  opacity: 1;
}

.c-input-checkbox--error .c-input-checkbox__label {
  --text-opacity: 1;
  color: #e71921;
  color: rgba(231, 25, 33, var(--text-opacity));
}

.c-input-checkbox--error .c-input-checkbox__label:before {
  border: 1px solid #e71921;
}

.c-input-checkbox--lg .c-input-checkbox__label {
  position: relative;
  display: block;
  padding: 0px 10px 0px 35px;
  cursor: pointer;
}

/* Pseudo checkbox */

.c-input-checkbox--lg .c-input-checkbox__label:before {
  content: "";
  position: absolute;
  left: 0;
  top: 2px;
  height: 24px;
  width: 24px;
  border: 1px solid #595959;
  border-radius: 2px;
  background: #fff;
}

/* Pseudo checkmark */

.c-input-checkbox--lg input + .c-input-checkbox__label:after {
  content: "\2714";
  position: absolute;
  left: 4px;
  top: 3px;
  height: auto;
  font-size: 20px;
  line-height: 20px;
  opacity: 0;
  transition: all 200ms ease-in;
}

.c-input-checkbox--lg input:checked + .c-input-checkbox__label:after {
  opacity: 1;
}

.c-input-checkbox--lg input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.c-input-checkbox--lg.c-input-checkbox--error .c-input-checkbox__label {
  color: #000;
}

.c-input-checkbox--lg.c-input-checkbox--error .c-input-checkbox__label:before {
  border: 1px solid #e71921;
}

.c-input-datepicker {
  display: flex;
  flex-direction: column;
  position: relative;
}
.c-input-datepicker__label {
  font-size: 12px;
  margin-bottom: 5px;
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
}
.c-input-datepicker__field {
  font-size: 14px;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  border-width: 1px;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
  border-radius: 0.125rem;
  padding: 10px;
  margin-top: 5px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: 3px;
  padding: 5px 10px 5px 10px;
  height: 44px;
  transition: all 200ms linear;
}
.c-input-datepicker__icon {
  display: block;
  position: absolute;
  right: 20px;
  top: 45px;
  width: 16px;
  height: auto;
  pointer-events: none;
}
@media (min-width: 1024px) {
  .c-input-datepicker__icon {
    top: 40px;

    width: 20px;
  }
}
.c-input-datepicker__helper {
  font-size: 12px;
  font-weight: 700;
  margin-top: 5px;
  --text-opacity: 1;
  color: #e71921;
  color: rgba(231, 25, 33, var(--text-opacity));
  transition: all 200ms linear;
}
.c-input-datepicker__tooltip {
  padding: 10px;
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
  position: absolute;
  bottom: 80px;
  height: auto;
  right: -10px;
  border: 1px solid #d8d8d8;
  width: 300px;
}
.c-input-datepicker__tooltip::before,
.c-input-datepicker__tooltip::after {
  content: "";
  position: absolute;
  top: 100%;
  right: 20px;
  border-width: 20px;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
  border-bottom: 20px solid transparent;
}
.c-input-datepicker__tooltip::before {
  border-top: 20px solid #d8d8d8;
  margin-top: 1px;
}
.c-input-datepicker__tooltip::after {
  border-top: 20px solid white;
}
.c-input-datepicker .vdp-datepicker__calendar {
  width: 100%;
  border: none;
}
.c-input-datepicker .vdp-datepicker__calendar .up {
  font-size: 16px;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  font-weight: 700;
}
.c-input-datepicker .vdp-datepicker__calendar .next::after,
.c-input-datepicker .vdp-datepicker__calendar .prev::after,
.c-input-datepicker .vdp-datepicker__calendar .next.disabled::after,
.c-input-datepicker .vdp-datepicker__calendar .prev.disabled::after {
  border-width: 1px;
  --border-opacity: 1;
  border-color: #e71921;
  border-color: rgba(231, 25, 33, var(--border-opacity));
  border-width: 3px;
  border-radius: 2px;
  height: 13px;
  width: 13px;
  transform: rotate(45deg) translate(-10px);
}
.c-input-datepicker .vdp-datepicker__calendar .next::after,
.c-input-datepicker .vdp-datepicker__calendar .next.disabled::after {
  border-left: transparent;
  border-bottom: transparent;
}
.c-input-datepicker .vdp-datepicker__calendar .prev::after,
.c-input-datepicker .vdp-datepicker__calendar .prev.disabled::after {
  border-right: transparent;
  border-top: transparent;
}
.c-input-datepicker .vdp-datepicker__calendar .next.disabled::after,
.c-input-datepicker .vdp-datepicker__calendar .prev.disabled:after {
  border-color: #d8d8d8;
}
.c-input-datepicker .vdp-datepicker__calendar .day-header {
  --text-opacity: 1;
  color: #999;
  color: rgba(153, 153, 153, var(--text-opacity));
  font-weight: 700;
}
.c-input-datepicker
  .vdp-datepicker__calendar
  .cell:not(.blank):not(.disabled).day:hover {
  border-width: 1px;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
}
.c-input-datepicker .vdp-datepicker__calendar .cell.day.today {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
}
.c-input-datepicker .vdp-datepicker__calendar .cell.selected,
.c-input-datepicker .vdp-datepicker__calendar .cell.selected:hover,
.c-input-datepicker .vdp-datepicker__calendar .cell.selected.today {
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
  font-weight: 700;
}
@media (min-width: 1024px) {
  .c-input-datepicker .vdp-datepicker__calendar .cell.day.sun {
    --text-opacity: 1;

    color: #e71921;

    color: rgba(231, 25, 33, var(--text-opacity));
  }
}
.c-input-datepicker .vdp-datepicker__calendar .cell.day.disabled {
  --text-opacity: 1;
  color: #d8d8d8;
  color: rgba(216, 216, 216, var(--text-opacity));
}

.c-input-dropdown {
  display: flex;
  flex-direction: column;
  position: relative;
}
.c-input-dropdown__label {
  font-size: 12px;
  margin-bottom: 5px;
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
}
.c-input-dropdown__field {
  font-size: 14px;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  border-width: 1px;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
  border-radius: 0.125rem;
  padding: 10px;
  margin-top: 5px;
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: 3px;
  padding: 5px 10px 5px 10px;
  height: 44px;
  transition: all 200ms linear;
}
.c-input-dropdown__chevron {
  display: block;
  position: absolute;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
  width: 16px;
  height: auto;
  pointer-events: none;
}
.c-input-dropdown__helper {
  font-size: 12px;
  font-weight: 700;
  margin-top: 5px;
  --text-opacity: 1;
  color: #e71921;
  color: rgba(231, 25, 33, var(--text-opacity));
  transition: all 200ms linear;
}

.c-input-dropdown--error {
  --border-opacity: 1;
  border-color: #e71921;
  border-color: rgba(231, 25, 33, var(--border-opacity));
}

.c-input-dropdown--error-bg {
  --border-opacity: 1;
  border-color: #e71921;
  border-color: rgba(231, 25, 33, var(--border-opacity));
  --bg-opacity: 1;
  background-color: #fdf3f3;
  background-color: rgba(253, 243, 243, var(--bg-opacity));
}

/* remove IE default arrow down style */

.c-input-dropdown > select::-ms-expand {
  display: none;
}

.c-input-text {
  display: flex;
  flex-direction: column;
  position: relative;
}
.c-input-text__field {
  transition: all 200ms linear;
}

.c-input-text__label .v-popover {
  top: 0;
}

.c-input-radio {
  position: relative;
}
.c-input-radio input {
  content: " ";
  border: 1px solid;
  border-radius: 100%;
  position: absolute;
  top: 7px;
  left: 0;
  height: 15px;
  width: 15px;
  opacity: 0.00001;
  display: block;
  background: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  pointer-events: none;
  z-index: 2;
}
label.c-input-radio__label {
  position: relative;
  height: 28px;
  padding: 5px 10px 5px 25px;
  display: block;
  transition: all 200ms ease-in;
  margin-bottom: 0;
}
.c-input-radio__label:before {
  content: "";
  position: absolute;
  left: 0;
  top: 7px;
  height: 14px;
  width: 14px;
  border: 1px solid #595959;
  border-radius: 50%;
}
input:focus + .c-input-radio__label:before {
  box-shadow: 0 0 0 2px #228bec;
}
input + .c-input-radio__label:after {
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
  content: "";
  position: absolute;
  left: 3px;
  top: 10px;
  height: 8px;
  width: 8px;
  border-radius: 50%;
  opacity: 0;
  transition: all 200ms ease-in;
}
input:checked + .c-input-radio__label:after {
  opacity: 1;
}

.c-input-radio-button {
  position: relative;
}

.c-input-radio-button input {
  content: " ";
  border: 1px solid;
  border-radius: 100%;
  position: absolute;
  top: 7px;
  left: 0;
  height: 15px;
  width: 15px;
  opacity: 0.00001;
  display: block;
  background: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  pointer-events: none;
  z-index: 2;
}

.c-input-radio-button__label {
  padding-left: 20px;
  padding-right: 20px;
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  font-size: 16px;
  font-weight: 700;
  display: inline-flex;
  align-content: center;
  justify-content: center;
  align-items: center;
  line-height: 1.25rem;
  border-width: 1px;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
  height: 44px;
  min-width: 170px;
  border-radius: 3px;
  transition: all 200ms ease-in;
}

.c-input-radio-button__label:hover {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.c-input-radio-button__label:before {
  content: none;
}

.c-input-radio-button__label:after {
  content: none;
}

.c-input-radio-button__label:after {
  content: none;
}

@media (min-width: 1024px) {
  .c-input-radio-button__label {
    min-width: 104px;
  }
}

.c-input-radio-button input:checked ~ label,
.c-input-radio-button input:checked ~ label:hover {
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
}

.c-input-radio-button input:checked ~ svg path,
.c-input-radio-button input:checked ~ svg path ~ polygon {
  fill: #333366;
}

.c-input-radio-button input:focus ~ label {
  outline: 5px auto Highlight; /* Firefox */
  outline: 5px auto -webkit-focus-ring-color; /* Chrome */
}

.c-input-radio-button--alt .c-input-radio-button__label {
  font-size: 12px;
  width: 100%;
  font-weight: 400;
}

.c-input-label {
  font-size: 12px;
  margin-bottom: 5px;
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
}

.c-input-helper {
  font-size: 12px;
  font-weight: 700;
  margin-top: 5px;
  --text-opacity: 1;
  color: #e71921;
  color: rgba(231, 25, 33, var(--text-opacity));
}

.c-input-field {
  font-size: 14px;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  border-width: 1px;
  --border-opacity: 1;
  border-color: #333366;
  border-color: rgba(51, 51, 102, var(--border-opacity));
  border-radius: 0.125rem;
  padding: 10px;
  margin-top: 5px;
  border-radius: 3px;
  padding: 5px 10px 5px 10px;
  height: 44px;
}

.c-input-field--error {
  --border-opacity: 1;
  border-color: #e71921;
  border-color: rgba(231, 25, 33, var(--border-opacity));
  --bg-opacity: 1;
  background-color: #fdf3f3;
  background-color: rgba(253, 243, 243, var(--bg-opacity));
}

.c-input-radio__group-label {
  font-size: 12px;
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
  margin-bottom: 5px;
  font-weight: 700;
}

.c-link {
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  font-weight: 700;
}
.c-link :hover {
  text-decoration: none;
}

.c-link--disabled {
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
  font-weight: 700;
}

.c-link--disabled :hover {
  text-decoration: none;
}

.c-link--inline {
  --text-opacity: 1;
  color: #3573b1;
  color: rgba(53, 115, 177, var(--text-opacity));
  font-weight: 700;
  text-decoration: underline;
}

.c-link--inline:hover {
  text-decoration: none;
}

.c-modal {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  overflow-x: hidden;
  overflow-y: auto;
  z-index: 20;
}
@media (min-width: 1024px) {
  .c-modal {
    display: flex;

    flex-direction: column;

    justify-content: center;
  }
}

.c-modal__backdrop {
  background-color: rgba(0, 0, 0, 0.3);
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
}

.c-modal__dialog {
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
  position: relative;
  padding: 30px;
  border-radius: 3px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  min-width: 320px;
  width: calc(100% - 60px);
  max-width: 708px;
  margin: 50px auto;
  z-index: 2;
}

@media (min-width: 1024px) {
  .c-modal__dialog {
    width: 100%;
  }
}

.c-modal__close {
  margin-left: auto;
  margin-right: 0;
  display: block;
}

.c-modal--wide .c-modal__dialog {
  max-width: 1100px;
}

.c-navbar {
  position: fixed;
  display: flex;
  bottom: 0;
  left: 0;
  width: 100vw;
  height: 50px;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
  z-index: 12;
} /* Between 11 (offers tile checkbox) and 15 (Ampersend SDK) */
.c-navbar .c-btn {
  height: 50px;
  flex: 1;
  border-radius: 0;
}
.c-navbar .c-btn--secondary {
  height: 50px;
  border: none;
}

.c-progress-bar {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  padding-top: 28px;
}

.c-progress-bar__copy {
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
  font-weight: 700;
  font-size: 14px;
  position: absolute;
  top: -28px;
  left: 0;
  right: 0;
  text-align: center;
  display: block;
  flex-basis: 100%;
}

.c-progress-bar__step {
  position: relative;
  flex-basis: 10px;
  flex-grow: 1;
  margin-right: 8px;
}

.c-progress-bar__step:last-child {
  margin-right: 0px;
}

.c-progress-bar__step::after {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
  width: 100%;
  display: inline-block;
  content: "";
  height: 12px;
  transform: skew(-20deg);
}

@media (min-width: 1024px) {
  .c-progress-bar__step::after {
    height: 19px;
  }
}

.c-progress-bar__step--active::after {
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
}

.c-progress-bar__step--short,
.c-progress-bar__step--short.c-progress-bar__step::after {
  height: 12px;
}

.c-street-dropdown,
.c-dropdown {
  position: absolute;
  border-width: 1px;
  border-radius: 0.25rem;
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
  font-size: 12px;
  top: 72px;
  left: 0;
  right: 0;
  z-index: 10;
  max-height: 150px;
  overflow-y: auto;
}

.c-street-dropdown__option,
.c-dropdown__option {
  padding: 10px;
  border-width: 1px;
  border-top: 0;
  border-left: 0;
  border-right: 0;
  cursor: pointer;
}

.c-street-dropdown__option.c-dropdown__option-focused,
.c-street-dropdown__option:hover,
.c-dropdown__option.c-dropdown__option-focused,
.c-dropdown__option:hover {
  --bg-opacity: 1;
  background-color: #f7f7f7;
  background-color: rgba(247, 247, 247, var(--bg-opacity));
}

.c-street-dropdown__option:last-of-type,
.c-dropdown__option:last-of-type {
  border-bottom: 0;
}

.c-tooltip {
  display: flex;
  flex-direction: row;
  position: relative;
}
.c-tooltip__pass-through {
  flex: 1 1 auto;
}
.c-tooltip::after {
  content: "";
  flex-basis: 30px;
}

.v-popover {
  position: absolute;
  right: 0;
  z-index: 10;
  top: 5px;
}

.tooltip {
  display: block !important;
  z-index: 25;
}

.tooltip li {
  margin-left: 25px;
  padding-left: 10px;
  list-style-type: disc;
}

.tooltip .tooltip-inner {
  padding: 15px;
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
  border-radius: 5px;
  border: solid grey 2px;
  box-sizing: border-box;
  color: black;
  max-width: 72vw;
}

.tooltip .tooltip-arrow {
  width: 0px;
  height: 0px;
  margin: 5px;
  border-style: solid;
  position: absolute;
  border-color: grey;
  z-index: 4;
}

.tooltip .tooltip-arrow:after {
  width: 0px;
  height: 0px;
  content: "";
  position: absolute;
  border-color: white;
  border-style: solid;
  z-index: 5;
}

.tooltip[x-placement^="top"] {
  margin-bottom: 5px;
}

.tooltip[x-placement^="top"] .tooltip-arrow {
  margin-top: 0px;
  margin-bottom: 0px;
  border-width: 20px 20px 0 20px;
  border-left-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
  bottom: -20px;
  left: calc(50% - 20px);
}

.tooltip[x-placement^="top"] .tooltip-arrow:after {
  bottom: 3px;
  left: calc(50% - 20px);
  border-width: inherit;
  border-left-color: inherit;
  border-right-color: inherit;
  border-bottom-color: inherit;
}

.tooltip[x-placement^="bottom"] {
  margin-top: 5px;
}

.tooltip[x-placement^="bottom"] .tooltip-arrow {
  margin-top: 0px;
  margin-bottom: 0px;
  border-width: 0 20px 20px 20px;
  border-left-color: transparent;
  border-right-color: transparent;
  border-top-color: transparent;
  top: -20px;
  left: calc(50% - 20px);
}

.tooltip[x-placement^="bottom"] .tooltip-arrow:after {
  top: 3px;
  left: calc(50% - 20px);
  border-width: inherit;
  border-left-color: inherit;
  border-right-color: inherit;
  border-top-color: inherit;
}

.tooltip[x-placement^="right"] {
  margin-left: 5px;
}

.tooltip[x-placement^="right"] .tooltip-arrow {
  margin-left: 0px;
  margin-right: 0px;
  border-width: 20px 20px 20px 0;
  border-left-color: transparent;
  border-top-color: transparent;
  border-bottom-color: transparent;
  left: -20px;
  top: calc(50% - 20px);
}

.tooltip[x-placement^="right"] .tooltip-arrow:after {
  left: 3px;
  top: calc(50% - 20px);
  border-width: inherit;
  border-left-color: inherit;
  border-top-color: inherit;
  border-bottom-color: inherit;
}

.tooltip[x-placement^="left"] {
  margin-right: 5px;
}

.tooltip[x-placement^="left"] .tooltip-arrow {
  margin-left: 0px;
  margin-right: 0px;
  border-width: 20px 0 20px 20px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
  right: -20px;
  top: calc(50% - 20px);
}

.tooltip[x-placement^="left"] .tooltip-arrow:after {
  right: 3px;
  top: calc(50% - 20px);
  border-width: inherit;
  border-top-color: inherit;
  border-right-color: inherit;
  border-bottom-color: inherit;
}

.tooltip[aria-hidden="true"] {
  visibility: hidden;
  opacity: 0;
  transition: opacity 0.15s, visibility 0.15s;
}

.tooltip[aria-hidden="false"] {
  visibility: visible;
  opacity: 1;
  transition: opacity 0.15s;
}

.access-disabled__img-wrapper {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  width: 250px;
  min-width: 250px;
  height: auto;
  padding: 85px 65px;
  background: #3949ab;
}
.access-disabled__img {
  height: auto;
  width: 120px;
  height: auto;
}
.access-disabled__heading {
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  font-weight: 700;
  font-size: 24px;
  line-height: 29px;
}
.access-disabled__copy {
  font-size: 14px;
  line-height: 20px;
}
@media screen and (min-width: 480px) {
  .access-disabled__copy {
    font-size: 16px;

    line-height: 22px;
  }
}
.access-disabled__legal {
  text-align: center;
  font-size: 12px;
  line-height: 18px;
}

.app-loader {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  text-align: center;
}
.app-loader__container {
  width: 100%;
}
@media (min-width: 1024px) {
  .app-loader__container {
    width: 20%;
  }
}
.app-loader__message {
  font-size: 22px;
}

.grecaptcha > .grecaptcha-badge {
  z-index: 50;
  bottom: 60px !important;
}
@media (min-width: 1024px) {
  .grecaptcha > .grecaptcha-badge {
    bottom: 14px !important;
  }
}

.modal-offers-delivery .c-btn,
.modal-offers-delivery .c-input-radio__label {
  width: 185px;
}

.modal-offers-text__actions {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
}
@media screen and (min-width: 480px) {
  .modal-offers-text__actions {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-direction: row;
    flex-direction: row;

    -webkit-box-pack: center;

    -ms-flex-pack: center;

    justify-content: center;
  }
}
.modal-offers-text__cta:last-of-type {
  margin-top: 20px;
}
@media screen and (min-width: 480px) {
  .modal-offers-text__cta:last-of-type {
    margin-top: 0px;

    margin-left: 20px;
  }
}

.modal-success-page {
  padding: 0;
}
@media (min-width: 1024px) {
  .modal-success-page {
    padding: 30px 60px 60px 60px;
  }
}
.modal-success-page svg {
  position: static;
  width: auto;
  height: auto;
  padding: 0;
  margin: 0;
  overflow: visible;
  clip: auto;
  white-space: normal;
  width: 64px;
  height: 64px;
}
.modal-success-page__heading {
  font-size: 16px;
  font-weight: 700;
}
@media (min-width: 1024px) {
  .modal-success-page__heading {
    font-size: 22px;
  }
}
.modal-success-page__actions {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.red-arrow {
  display: inline-block;
  height: 16px;
  width: 16px;
  border-right: 3px solid #e71921;
  border-top: 3px solid #e71921;
  border-radius: 2px;
  background-color: transparent;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

@-webkit-keyframes fadeControlIn {
  0% {
    opacity: 0;
  }

  75% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes fadeControlIn {
  0% {
    opacity: 0;
  }

  75% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

.fade-control-in {
  min-height: 250px;
  -webkit-animation-name: fadeControlIn;
  animation-name: fadeControlIn;
  -webkit-animation-duration: 0.5s;
  animation-duration: 0.5s;
}

@media (min-width: 1024px) {
  .fade-control-in {
    min-height: 400px;
  }
}

.page__action .app-footer {
  display: none;
}

.age-verification__icon-lock {
  display: inline-block;
  position: absolute;
  top: 2px;
  width: 13px;
  height: 17px;
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAgCAYAAAABtRhCAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHKADAAQAAAABAAAAIAAAAAAAbKElAAABfElEQVRIDeWWO04DQRBEzUdwAr4pXAIJEogR4gjcxjEgUk7BBUxOAgEnYEmBCAKgnrVrW+3yzg62VwJaKrmnurp6Nd4Zu9NpFguSHQvXwqPwVoIcjhqamcSeXO6ErwTQoJ0qztT9IaSGVfV3aen5UZyo61OozJp+0kNvVmxI/So0HRJ19OLROC6ljCasH4RTYasEOZzT4tEoVqR6EaLJjbhV4wBHLerxwCsZR1K45s2aTmruIQ9jz2IktN4xXE/cs+ErihqaGLuRcAPXo0jre8NFymnGvNzA5eikNWcxFU4z5uUGpoynqv/9gWwPZ6UrPAnxOMxqjTcz+ueSZFbGKZ8uv2FM56pqIwoG8lStxa94Sy+0HdslyLMj9UWP1m+NO9yopjbP3dJJA81zeCp3oLsvHeenic0dONGoaSF3YP+mCOaOC5LhMnfgwbB1kDluUHRJ7Vulhlg/F1f9iSKP9dr1/7hpCrfPc+KKJRmvCftzGhBtryB4rVv7Af4GyZvvA6CseswAAAAASUVORK5CYII=);
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
}
@media screen and (min-width: 480px) {
  .age-verification__icon-lock {
    top: 1px;

    width: 16px;

    height: 21px;
  }
}

.confirm-order__vr-image-wrapper {
  -webkit-box-flex: 0;
  -ms-flex: 0 0 200px;
  flex: 0 0 200px;
}
.confirm-order__vr-image {
  width: 200px;
  height: 200px;
}

.confirm-order.desktop {
  /* End offers */
}

/* Start voter reg */

.confirm-order.desktop .amp-vr {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  width: 100%;
  height: 100%;
  padding: 50px;
  padding-right: 100px;
  --bg-opacity: 1;
  background-color: #f7f7f7;
  background-color: rgba(247, 247, 247, var(--bg-opacity));
}

.confirm-order.desktop .amp-vr__image-wrapper {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-flex: 0;
  -ms-flex-positive: 0;
  flex-grow: 0;
  -ms-flex-negative: 0;
  flex-shrink: 0;
  -ms-flex-preferred-size: auto;
  flex-basis: auto;
  width: 150px;
  max-width: 150px;
  height: 138px;
}

.confirm-order.desktop .amp-vr__content {
  margin-left: 50px;
  width: 100%;
}

.confirm-order.desktop .amp-vr__heading {
  font-size: 22px;
  font-weight: 700;
  line-height: 27px;
}

.confirm-order.desktop .amp-vr__body {
  font-size: 16px;
  line-height: 22px;
}

.confirm-order.desktop .amp-vr__checkbox-wrapper {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  padding: 20px;
  border-width: 1px;
  border-style: dashed;
  --border-opacity: 1;
  border-color: #000;
  border-color: rgba(0, 0, 0, var(--border-opacity));
}

.confirm-order.desktop .amp-vr__checkbox-heading {
  margin-top: 0px;
  margin-bottom: 10px;
  font-weight: 700;
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
  font-size: 16px;
  line-height: 19px;
}

.confirm-order.desktop .amp-vr__copy-sm {
  font-size: 13px;
  line-height: 19px;
}

.confirm-order.desktop .sp-modal {
  font-size: 14px;
  padding: 30px 60px 60px 60px;
}

.confirm-order.desktop .sp-modal__heading {
  font-size: 22px;
  font-weight: 700;
}

.confirm-order.desktop .sp-modal__actions {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

/* Start offers */

.confirm-order.desktop .amp-offers {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  width: 100%;
  height: 100%;
  padding: 50px;
  padding-right: 100px;
  --bg-opacity: 1;
  background-color: #f7f7f7;
  background-color: rgba(247, 247, 247, var(--bg-opacity));
}

/* End voter reg */

.confirm-order.desktop .amp-offers__left-col {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-flex: 0;
  -ms-flex-positive: 0;
  flex-grow: 0;
  -ms-flex-negative: 0;
  flex-shrink: 0;
  -ms-flex-preferred-size: auto;
  flex-basis: auto;
  width: 180px;
  max-width: 180px;
}

.confirm-order.desktop .amp-offers__image-wrapper {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  height: 60px;
}

.confirm-order.desktop .amp-offers__image-wrapper--h-auto {
  height: auto;
}

.confirm-order.desktop .amp-offers__image {
  height: auto;
  max-width: 100%;
}

.confirm-order.desktop .amp-offers__content {
  margin-left: 50px;
  max-width: 800px;
}

.confirm-order.desktop .amp-offers__heading {
  font-size: 22px;
  font-weight: 700;
  line-height: 27px;
}

.confirm-order.desktop .amp-offers__body {
  font-size: 16px;
  line-height: 22px;
}

.confirm-order.desktop .amp-offers__text-sm {
  font-size: 13px;
  line-height: 19px;
}

/* Start offers */

.confirm-order.mobile .amp-offers__heading {
  font-weight: 700;
  font-size: 18px;
  line-height: 22px;
}

.confirm-order.mobile .amp-offers__body {
  font-size: 14px;
  line-height: 20px;
}

.confirm-order.mobile .amp-offers__autofill-copy {
  font-size: 13px;
  line-height: 19px;
}

.confirm-order.mobile .amp-offers__legal {
  font-size: 10px;
  line-height: 16px;
}

/* Start voter reg */

.confirm-order.mobile .amp-vr__heading {
  font-weight: 700;
  font-size: 18px;
  line-height: 22px;
}

/* End offers */

.confirm-order.mobile .amp-vr__body {
  font-size: 14px;
  line-height: 20px;
}

.confirm-order.mobile .amp-vr__copy {
  font-size: 13px;
  line-height: 19px;
}

.confirm-order.mobile .amp-vr__legal {
  font-size: 10px;
  line-height: 16px;
}

.confirm-order.mobile .sp-modal__heading {
  font-weight: 700;
  font-size: 16px;
  line-height: 22px;
}

.confirm-order.mobile .sp-modal__actions {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.disclaimer-desktop {
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
}
.disclaimer-desktop__header {
  background-size: cover;
  background: -webkit-gradient(
      linear,
      left top,
      left bottom,
      color-stop(100%, rgba(51, 51, 102, 0.7)),
      to(rgba(51, 51, 102, 0.7))
    ),
    url(/img/usps-purple-lifestyle.ccfccfe6.jpg);
  background: linear-gradient(
      rgba(51, 51, 102, 0.7) 100%,
      rgba(51, 51, 102, 0.7) 100%
    ),
    url(/img/usps-purple-lifestyle.ccfccfe6.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}
@media (min-width: 1024px) {
  .disclaimer-desktop__header {
    background-position: top 33% center;
  }
}
.disclaimer-desktop__header-h1 {
  font-weight: 700;
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
  margin-bottom: 30px;
}
.disclaimer-desktop__cta {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: distribute;
  justify-content: space-around;
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
}
.disclaimer-desktop__cta-item {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  padding-left: 25px;
  padding-right: 25px;
  padding-top: 20px;
  padding-bottom: 20px;
  -webkit-box-flex: 0;
  -ms-flex: 0 0 33.3%;
  flex: 0 0 33.3%;
}
@media (min-width: 1380px) {
  .disclaimer-desktop__cta-item {
    padding-left: 45px;

    padding-right: 45px;

    padding-top: 30px;

    padding-bottom: 30px;
  }
}
.disclaimer-desktop__cta-item:first-of-type {
  padding-left: 0px;
}
.disclaimer-desktop__cta-item:nth-of-type(odd) {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
}
.disclaimer-desktop__cta-item:nth-of-type(even) {
  --bg-opacity: 1;
  background-color: #f7f7f7;
  background-color: rgba(247, 247, 247, var(--bg-opacity));
  -webkit-transform: skew(-13deg);
  transform: skew(-13deg);
}
.disclaimer-desktop__cta-item:nth-of-type(even) img,
.disclaimer-desktop__cta-item:nth-of-type(even) div {
  -webkit-transform: skew(13deg);
  transform: skew(13deg);
}
.disclaimer-desktop__cta-item:last-of-type {
  padding-right: 0px;
}
.disclaimer-desktop__cta-icon {
  display: inline-block;
  vertical-align: middle;
  margin-top: 5px;
  margin-right: 20px;
  height: 42px;
  width: 42px;
}
.disclaimer-desktop__cta-text {
  display: inline-block;
  vertical-align: middle;
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
  width: calc(100% - 62px);
}

.disclaimer-mobile__get-started-text {
  padding: 10px;
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
  font-size: 12px;
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
  text-align: center;
  -webkit-box-shadow: 0 0 5px 1px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 5px 1px rgba(0, 0, 0, 0.2);
}

.page__disclaimer .app-footer {
  padding-bottom: 156px;
}

@media (min-width: 1024px) {
  .page__disclaimer .app-footer {
    padding-bottom: 30px;
  }
}

.instant-savings-desktop__offers-cta {
  width: 225px;
}
.instant-savings-desktop__offer-tile {
  margin: 2px;
}

/* correction for style bleed */

.page__instant-savings .mva-print__barcode img {
  display: inline-block;
}

.instant-savings-mobile__offer-tile {
  margin: 2px;
}

.offer-details {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
}

@media print {
  .page__offer-details .app-header-desktop,
  .page__offer-details .app-footer {
    display: none;
  }
}

/* correction for style bleed */

.page__offer-details .mva-print__barcode img,
.page__offer-details .mva-mobile-full-page__barcode img {
  display: inline-block;
}

.page__simulator {
  width: 100vw;
  height: 100vh;
}
.page__simulator .app-header-desktop,
.page__simulator .app-header-mobile,
.page__simulator .app-footer {
  display: none;
}

.page__sms-return-to-site .app-footer {
  display: none;
}
/* correction for style bleed */
.page__sms-return-to-site .mva-mobile-full-page__barcode img {
  display: inline-block;
}

.u-container {
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
  padding-right: 20px;
}
@media (min-width: 1024px) {
  .u-container {
    width: 100%;

    padding-top: 50px;

    padding-bottom: 50px;

    padding-left: 100px;

    padding-right: 100px;
  }
}
@media (min-width: 1380px) {
  .u-container {
    max-width: 1180px;

    margin-left: auto;

    margin-right: auto;

    padding-top: 50px;

    padding-bottom: 50px;

    padding-left: 0px;

    padding-right: 0px;
  }
}

.u-container--x {
  padding-left: 20px;
  padding-right: 20px;
}

@media (min-width: 1024px) {
  .u-container--x {
    width: 100%;

    padding-left: 100px;

    padding-right: 100px;
  }
}

@media (min-width: 1380px) {
  .u-container--x {
    max-width: 1180px;

    margin-left: auto;

    margin-right: auto;

    padding-left: 0px;

    padding-right: 0px;
  }
}

@media (min-width: 1024px) {
  .u-static-container {
    max-width: 768px;
  }
}

.u-print-only {
  display: none;
}
@media print {
  .u-print-only {
    display: block;
  }
}

@media print {
  .u-no-print {
    display: none;
  }
}

/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */

/* Document
   ========================================================================== */

/**
 * 1. Correct the line height in all browsers.
 * 2. Prevent adjustments of font size after orientation changes in iOS.
 */

html {
  line-height: 1.15; /* 1 */
  -webkit-text-size-adjust: 100%; /* 2 */
}

/* Sections
   ========================================================================== */

/**
 * Remove the margin in all browsers.
 */

body {
  margin: 0;
}

/**
 * Render the `main` element consistently in IE.
 */

main {
  display: block;
}

/**
 * Correct the font size and margin on `h1` elements within `section` and
 * `article` contexts in Chrome, Firefox, and Safari.
 */

h1 {
  font-size: 2em;
  margin: 0.67em 0;
}

/* Grouping content
   ========================================================================== */

/**
 * 1. Add the correct box sizing in Firefox.
 * 2. Show the overflow in Edge and IE.
 */

hr {
  -webkit-box-sizing: content-box;
  box-sizing: content-box; /* 1 */
  height: 0; /* 1 */
  overflow: visible; /* 2 */
}

/**
 * 1. Correct the inheritance and scaling of font size in all browsers.
 * 2. Correct the odd `em` font sizing in all browsers.
 */

pre {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
}

/* Text-level semantics
   ========================================================================== */

/**
 * Remove the gray background on active links in IE 10.
 */

a {
  background-color: transparent;
}

/**
 * 1. Remove the bottom border in Chrome 57-
 * 2. Add the correct text decoration in Chrome, Edge, IE, Opera, and Safari.
 */

abbr[title] {
  border-bottom: none; /* 1 */
  text-decoration: underline; /* 2 */
  -webkit-text-decoration: underline dotted;
  text-decoration: underline dotted; /* 2 */
}

/**
 * Add the correct font weight in Chrome, Edge, and Safari.
 */

b,
strong {
  font-weight: bolder;
}

/**
 * 1. Correct the inheritance and scaling of font size in all browsers.
 * 2. Correct the odd `em` font sizing in all browsers.
 */

code,
kbd,
samp {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
}

/**
 * Add the correct font size in all browsers.
 */

small {
  font-size: 80%;
}

/**
 * Prevent `sub` and `sup` elements from affecting the line height in
 * all browsers.
 */

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sub {
  bottom: -0.25em;
}

sup {
  top: -0.5em;
}

/* Embedded content
   ========================================================================== */

/**
 * Remove the border on images inside links in IE 10.
 */

img {
  border-style: none;
}

/* Forms
   ========================================================================== */

/**
 * 1. Change the font styles in all browsers.
 * 2. Remove the margin in Firefox and Safari.
 */

button,
input,
optgroup,
select,
textarea {
  font-family: inherit; /* 1 */
  font-size: 100%; /* 1 */
  line-height: 1.15; /* 1 */
  margin: 0; /* 2 */
}

/**
 * Show the overflow in IE.
 * 1. Show the overflow in Edge.
 */

button,
input {
  /* 1 */
  overflow: visible;
}

/**
 * Remove the inheritance of text transform in Edge, Firefox, and IE.
 * 1. Remove the inheritance of text transform in Firefox.
 */

button,
select {
  /* 1 */
  text-transform: none;
}

/**
 * Correct the inability to style clickable types in iOS and Safari.
 */

button,
[type="button"],
[type="reset"],
[type="submit"] {
  -webkit-appearance: button;
}

/**
 * Remove the inner border and padding in Firefox.
 */

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner {
  border-style: none;
  padding: 0;
}

/**
 * Restore the focus styles unset by the previous rule.
 */

button:-moz-focusring,
[type="button"]:-moz-focusring,
[type="reset"]:-moz-focusring,
[type="submit"]:-moz-focusring {
  outline: 1px dotted ButtonText;
}

/**
 * Correct the padding in Firefox.
 */

fieldset {
  padding: 0.35em 0.75em 0.625em;
}

/**
 * 1. Correct the text wrapping in Edge and IE.
 * 2. Correct the color inheritance from `fieldset` elements in IE.
 * 3. Remove the padding so developers are not caught out when they zero out
 *    `fieldset` elements in all browsers.
 */

legend {
  -webkit-box-sizing: border-box;
  box-sizing: border-box; /* 1 */
  color: inherit; /* 2 */
  display: table; /* 1 */
  max-width: 100%; /* 1 */
  padding: 0; /* 3 */
  white-space: normal; /* 1 */
}

/**
 * Add the correct vertical alignment in Chrome, Firefox, and Opera.
 */

progress {
  vertical-align: baseline;
}

/**
 * Remove the default vertical scrollbar in IE 10+.
 */

textarea {
  overflow: auto;
}

/**
 * 1. Add the correct box sizing in IE 10.
 * 2. Remove the padding in IE 10.
 */

[type="checkbox"],
[type="radio"] {
  -webkit-box-sizing: border-box;
  box-sizing: border-box; /* 1 */
  padding: 0; /* 2 */
}

/**
 * Correct the cursor style of increment and decrement buttons in Chrome.
 */

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button {
  height: auto;
}

/**
 * 1. Correct the odd appearance in Chrome and Safari.
 * 2. Correct the outline style in Safari.
 */

[type="search"] {
  -webkit-appearance: textfield; /* 1 */
  outline-offset: -2px; /* 2 */
}

/**
 * Remove the inner padding in Chrome and Safari on macOS.
 */

[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}

/**
 * 1. Correct the inability to style clickable types in iOS and Safari.
 * 2. Change font properties to `inherit` in Safari.
 */

/* Interactive
   ========================================================================== */

/*
 * Add the correct display in Edge, IE 10+, and Firefox.
 */

details {
  display: block;
}

/*
 * Add the correct display in all browsers.
 */

summary {
  display: list-item;
}

/* Misc
   ========================================================================== */

/**
 * Add the correct display in IE 10+.
 */

template {
  display: none;
}

/**
 * Add the correct display in IE 10.
 */

/**
 * Manually forked from SUIT CSS Base: https://github.com/suitcss/base
 * A thin layer on top of normalize.css that provides a starting point more
 * suitable for web applications.
 */

/**
 * Removes the default spacing and border for appropriate elements.
 */

blockquote,
dl,
dd,
h1,
h2,
h3,
h4,
h5,
h6,
hr,
figure,
p,
pre {
  margin: 0;
}

button {
  background-color: transparent;
  background-image: none;
}

/**
 * Work around a Firefox/IE bug where the transparent `button` background
 * results in a loss of the default `button` focus styles.
 */

button:focus {
  outline: 1px dotted;
  outline: 5px auto -webkit-focus-ring-color;
}

fieldset {
  margin: 0;
  padding: 0;
}

ol,
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

/**
 * Tailwind custom reset styles
 */

/**
 * 1. Use the user's configured `sans` font-family (with Tailwind's default
 *    sans-serif font stack as a fallback) as a sane default.
 * 2. Use Tailwind's default "normal" line-height so the user isn't forced
 *    to override it to ensure consistency even when using the default theme.
 */

html {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji",
    "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"; /* 1 */
  line-height: 1.5; /* 2 */
}

/**
 * 1. Prevent padding and border from affecting element width.
 *
 *    We used to set this in the html element and inherit from
 *    the parent element for everything else. This caused issues
 *    in shadow-dom-enhanced elements like <details> where the content
 *    is wrapped by a div with box-sizing set to `content-box`.
 *
 *    https://github.com/mozdevs/cssremedy/issues/4
 *
 *
 * 2. Allow adding a border to an element by just adding a border-width.
 *
 *    By default, the way the browser specifies that an element should have no
 *    border is by setting it's border-style to `none` in the user-agent
 *    stylesheet.
 *
 *    In order to easily add borders to elements by just setting the `border-width`
 *    property, we change the default border-style for all elements to `solid`, and
 *    use border-width to hide them instead. This way our `border` utilities only
 *    need to set the `border-width` property instead of the entire `border`
 *    shorthand, making our border utilities much more straightforward to compose.
 *
 *    https://github.com/tailwindcss/tailwindcss/pull/116
 */

*,
::before,
::after {
  -webkit-box-sizing: border-box;
  box-sizing: border-box; /* 1 */
  border-width: 0; /* 2 */
  border-style: solid; /* 2 */
  border-color: #d8d8d8; /* 2 */
}

/*
 * Ensure horizontal rules are visible by default
 */

hr {
  border-top-width: 1px;
}

/**
 * Undo the `border-style: none` reset that Normalize applies to images so that
 * our `border-{width}` utilities have the expected effect.
 *
 * The Normalize reset is unnecessary for us since we default the border-width
 * to 0 on all elements.
 *
 * https://github.com/tailwindcss/tailwindcss/issues/362
 */

img {
  border-style: solid;
}

textarea {
  resize: vertical;
}

input::-webkit-input-placeholder,
textarea::-webkit-input-placeholder {
  color: #a0aec0;
}

input::-moz-placeholder,
textarea::-moz-placeholder {
  color: #a0aec0;
}

input:-ms-input-placeholder,
textarea:-ms-input-placeholder {
  color: #a0aec0;
}

input::-ms-input-placeholder,
textarea::-ms-input-placeholder {
  color: #a0aec0;
}

input::placeholder,
textarea::placeholder {
  color: #a0aec0;
}

button,
[role="button"] {
  cursor: pointer;
}

table {
  border-collapse: collapse;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-size: inherit;
  font-weight: inherit;
}

/**
 * Reset links to optimize for opt-in styling instead of
 * opt-out.
 */

a {
  color: inherit;
  text-decoration: inherit;
}

/**
 * Reset form element properties that are easy to forget to
 * style explicitly so you don't inadvertently introduce
 * styles that deviate from your design system. These styles
 * supplement a partial reset that is already applied by
 * normalize.css.
 */

button,
input,
optgroup,
select,
textarea {
  padding: 0;
  line-height: inherit;
  color: inherit;
}

/**
 * Use the configured 'mono' font family for elements that
 * are expected to be rendered with a monospace font, falling
 * back to the system monospace stack if there is no configured
 * 'mono' font family.
 */

pre,
code,
kbd,
samp {
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
    "Courier New", monospace;
}

/**
 * Make replaced elements `display: block` by default as that's
 * the behavior you want almost all of the time. Inspired by
 * CSS Remedy, with `svg` added as well.
 *
 * https://github.com/mozdevs/cssremedy/issues/14
 */

img,
svg,
video,
canvas,
audio,
iframe,
embed,
object {
  display: block;
  vertical-align: middle;
}

/**
 * Constrain images and videos to the parent width and preserve
 * their instrinsic aspect ratio.
 *
 * https://github.com/mozdevs/cssremedy/issues/14
 */

img,
video {
  max-width: 100%;
  height: auto;
}

html {
  font-family: Helvetica Neue, Arial, sans-serif;
}

body {
  font-family: Helvetica Neue, Arial, sans-serif;
}

h1 {
  font-size: 32px;
  color: #333366;
}

h2 {
  font-size: 28px;
  color: #333366;
}

h3 {
  font-size: 22px;
  color: #333366;
}

h4 {
  font-size: 18px;
  color: #333366;
}

h5 {
  font-size: 16px;
  color: #333366;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.not-sr-only {
  position: static;
  width: auto;
  height: auto;
  padding: 0;
  margin: 0;
  overflow: visible;
  clip: auto;
  white-space: normal;
}

.bg-white {
  --bg-opacity: 1;
  background-color: #fff;
  background-color: rgba(255, 255, 255, var(--bg-opacity));
}

.bg-gray-100 {
  --bg-opacity: 1;
  background-color: #f7f7f7;
  background-color: rgba(247, 247, 247, var(--bg-opacity));
}

.bg-gray-200 {
  --bg-opacity: 1;
  background-color: #ededed;
  background-color: rgba(237, 237, 237, var(--bg-opacity));
}

.bg-blue-200 {
  --bg-opacity: 1;
  background-color: #333366;
  background-color: rgba(51, 51, 102, var(--bg-opacity));
}

.rounded-none {
  border-radius: 0;
}

.block {
  display: block;
}

.inline {
  display: inline;
}

.flex {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.table {
  display: table;
}

.contents {
  display: contents;
}

.flex-row {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  -ms-flex-direction: row;
  flex-direction: row;
}

.flex-col {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
}

.flex-wrap {
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
}

.flex-no-wrap {
  -ms-flex-wrap: nowrap;
  flex-wrap: nowrap;
}

.items-center {
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.justify-center {
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
}

.justify-between {
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}

.flex-1 {
  -webkit-box-flex: 1;
  -ms-flex: 1 1 0%;
  flex: 1 1 0%;
}

.flex-auto {
  -webkit-box-flex: 1;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
}

.flex-grow {
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
}

.flex-shrink {
  -ms-flex-negative: 1;
  flex-shrink: 1;
}

.font-bold {
  font-weight: 700;
}

.h-full {
  height: 100%;
}

.text-xs {
  font-size: 10px;
}

.text-sm {
  font-size: 12px;
}

.text-base {
  font-size: 14px;
}

.text-lg {
  font-size: 16px;
}

.text-xl {
  font-size: 18px;
}

.text-2xl {
  font-size: 22px;
}

.list-disc {
  list-style-type: disc;
}

.list-decimal {
  list-style-type: decimal;
}

.m-auto {
  margin: auto;
}

.my-3 {
  margin-top: 15px;
  margin-bottom: 15px;
}

.my-5 {
  margin-top: 25px;
  margin-bottom: 25px;
}

.my-6 {
  margin-top: 30px;
  margin-bottom: 30px;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.-mx-4 {
  margin-left: -20px;
  margin-right: -20px;
}

.mt-1 {
  margin-top: 5px;
}

.mr-1 {
  margin-right: 5px;
}

.ml-1 {
  margin-left: 5px;
}

.mt-2 {
  margin-top: 10px;
}

.mr-2 {
  margin-right: 10px;
}

.ml-2 {
  margin-left: 10px;
}

.mt-3 {
  margin-top: 15px;
}

.mr-3 {
  margin-right: 15px;
}

.ml-3 {
  margin-left: 15px;
}

.mt-4 {
  margin-top: 20px;
}

.mr-4 {
  margin-right: 20px;
}

.mb-4 {
  margin-bottom: 20px;
}

.ml-4 {
  margin-left: 20px;
}

.mt-5 {
  margin-top: 25px;
}

.mr-5 {
  margin-right: 25px;
}

.mb-5 {
  margin-bottom: 25px;
}

.ml-5 {
  margin-left: 25px;
}

.mt-6 {
  margin-top: 30px;
}

.mr-6 {
  margin-right: 30px;
}

.mb-6 {
  margin-bottom: 30px;
}

.ml-6 {
  margin-left: 30px;
}

.mt-7 {
  margin-top: 35px;
}

.mt-8 {
  margin-top: 40px;
}

.ml-8 {
  margin-left: 40px;
}

.mb-9 {
  margin-bottom: 45px;
}

.mt-10 {
  margin-top: 50px;
}

.max-w-600 {
  max-width: 600px;
}

.max-w-1\/2 {
  max-width: 50%;
}

.min-h-screen {
  min-height: 100vh;
}

.overflow-hidden {
  overflow: hidden;
}

.p-0 {
  padding: 0px;
}

.p-4 {
  padding: 20px;
}

.p-6 {
  padding: 30px;
}

.p-10 {
  padding: 50px;
}

.py-0 {
  padding-top: 0px;
  padding-bottom: 0px;
}

.py-2 {
  padding-top: 10px;
  padding-bottom: 10px;
}

.py-4 {
  padding-top: 20px;
  padding-bottom: 20px;
}

.px-4 {
  padding-left: 20px;
  padding-right: 20px;
}

.py-6 {
  padding-top: 30px;
  padding-bottom: 30px;
}

.px-6 {
  padding-left: 30px;
  padding-right: 30px;
}

.py-8 {
  padding-top: 40px;
  padding-bottom: 40px;
}

.pb-0 {
  padding-bottom: 0px;
}

.pt-1 {
  padding-top: 5px;
}

.pr-4 {
  padding-right: 20px;
}

.pl-4 {
  padding-left: 20px;
}

.pl-5 {
  padding-left: 25px;
}

.pb-6 {
  padding-bottom: 30px;
}

.pb-10 {
  padding-bottom: 50px;
}

.pl-xl {
  padding-left: 100px;
}

.fixed {
  position: fixed;
}

.relative {
  position: relative;
}

.text-left {
  text-align: left;
}

.text-center {
  text-align: center;
}

.text-black {
  --text-opacity: 1;
  color: #000;
  color: rgba(0, 0, 0, var(--text-opacity));
}

.text-white {
  --text-opacity: 1;
  color: #fff;
  color: rgba(255, 255, 255, var(--text-opacity));
}

.text-gray-500 {
  --text-opacity: 1;
  color: #595959;
  color: rgba(89, 89, 89, var(--text-opacity));
}

.text-red-200 {
  --text-opacity: 1;
  color: #e71921;
  color: rgba(231, 25, 33, var(--text-opacity));
}

.text-red-300 {
  --text-opacity: 1;
  color: #f44336;
  color: rgba(244, 67, 54, var(--text-opacity));
}

.text-blue-100 {
  --text-opacity: 1;
  color: #3573b1;
  color: rgba(53, 115, 177, var(--text-opacity));
}

.text-blue-200 {
  --text-opacity: 1;
  color: #333366;
  color: rgba(51, 51, 102, var(--text-opacity));
}

.uppercase {
  text-transform: uppercase;
}

.underline {
  text-decoration: underline;
}

.align-top {
  vertical-align: top;
}

.invisible {
  visibility: hidden;
}

.w-2 {
  width: 10px;
}

.w-4 {
  width: 20px;
}

.w-1\/2 {
  width: 50%;
}

.w-2\/3 {
  width: 66.666667%;
}

.w-1\/5 {
  width: 20%;
}

.w-full {
  width: 100%;
}

.w-screen {
  width: 100vw;
}

.transform {
  --transform-translate-x: 0;
  --transform-translate-y: 0;
  --transform-rotate: 0;
  --transform-skew-x: 0;
  --transform-skew-y: 0;
  --transform-scale-x: 1;
  --transform-scale-y: 1;
  -webkit-transform: translateX(var(--transform-translate-x))
    translateY(var(--transform-translate-y)) rotate(var(--transform-rotate))
    skewX(var(--transform-skew-x)) skewY(var(--transform-skew-y))
    scaleX(var(--transform-scale-x)) scaleY(var(--transform-scale-y));
  transform: translateX(var(--transform-translate-x))
    translateY(var(--transform-translate-y)) rotate(var(--transform-rotate))
    skewX(var(--transform-skew-x)) skewY(var(--transform-skew-y))
    scaleX(var(--transform-scale-x)) scaleY(var(--transform-scale-y));
}

.transition {
  -webkit-transition-property: background-color, border-color, color, fill,
    stroke, opacity, -webkit-box-shadow, -webkit-transform;
  transition-property: background-color, border-color, color, fill, stroke,
    opacity, -webkit-box-shadow, -webkit-transform;
  transition-property: background-color, border-color, color, fill, stroke,
    opacity, box-shadow, transform;
  transition-property: background-color, border-color, color, fill, stroke,
    opacity, box-shadow, transform, -webkit-box-shadow, -webkit-transform;
}

@-webkit-keyframes spin {
  to {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes spin {
  to {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@-webkit-keyframes ping {
  75%,
  100% {
    -webkit-transform: scale(2);
    transform: scale(2);
    opacity: 0;
  }
}

@keyframes ping {
  75%,
  100% {
    -webkit-transform: scale(2);
    transform: scale(2);
    opacity: 0;
  }
}

@-webkit-keyframes pulse {
  50% {
    opacity: 0.5;
  }
}

@keyframes pulse {
  50% {
    opacity: 0.5;
  }
}

@-webkit-keyframes bounce {
  0%,
  100% {
    -webkit-transform: translateY(-25%);
    transform: translateY(-25%);
    -webkit-animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }

  50% {
    -webkit-transform: none;
    transform: none;
    -webkit-animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}

@keyframes bounce {
  0%,
  100% {
    -webkit-transform: translateY(-25%);
    transform: translateY(-25%);
    -webkit-animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }

  50% {
    -webkit-transform: none;
    transform: none;
    -webkit-animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}

@media (min-width: 640px) {
  .sm\:mb-0 {
    margin-bottom: 0px;
  }
}

@media (min-width: 768px) {
}

@media (min-width: 1024px) {
  .lg\:bg-white {
    --bg-opacity: 1;
    background-color: #fff;
    background-color: rgba(255, 255, 255, var(--bg-opacity));
  }

  .lg\:font-bold {
    font-weight: 700;
  }

  .lg\:m-0 {
    margin: 0px;
  }

  .lg\:mt-0 {
    margin-top: 0px;
  }

  .lg\:mb-0 {
    margin-bottom: 0px;
  }

  .lg\:mr-3 {
    margin-right: 15px;
  }

  .lg\:p-0 {
    padding: 0px;
  }

  .lg\:visible {
    visibility: visible;
  }

  .lg\:w-auto {
    width: auto;
  }
}

@media (min-width: 1280px) {
}

@media (min-width: 768px) {
  .tablet\:w-1\/2 {
    width: 50%;
  }
}

@media (min-width: 1024px) {
}

@media (min-width: 1380px) {
  .max\:pr-xl {
    padding-right: 100px;
  }
}
.amp-aside {
  position: fixed;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-top: 60px;
  top: 0;
  right: 0;
  width: 400px;
  height: 100vh;
  background-color: #32363d;
  transform: translateX(100%);
  transition: all 0.5s cubic-bezier(0.29, 0.67, 0.4, 0.95);
  z-index: 15;
}

@media screen and (max-width: 480px) {
  .amp-aside {
    width: 100%;
  }
}

.amp-aside:after {
  content: "";
  pointer-events: none;
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  box-shadow: 0 20px 60px -2px rgba(27, 33, 58, 0.8);
  transition: all 0.5s cubic-bezier(0.29, 0.67, 0.4, 0.95);
  opacity: 0;
}

.amp-aside.is-open {
  transform: translateX(0);
}

.amp-aside.is-open:after {
  opacity: 1;
}

@media screen and (max-width: 480px) {
  .amp-aside.is-open .amp-tab {
    left: 0;
  }
}

.amp-aside__upper {
  position: relative;
  flex: 0 1 80%;
  max-height: 80%;
  overflow: scroll;
}

.amp-aside__lower {
  position: relative;
}

.amp-header {
  position: absolute;
  top: 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #37474f;
  height: 5rem;
}

.amp-header__logo {
  width: 14rem;
  margin-left: 1rem;
}

.amp-header__logo .st0 {
  fill: #b0bec5;
}

.amp-header__logo .st1 {
  fill: #fa4238;
}

.amp-header__title {
  color: #b0bec5;
  font-family: Source Sans Pro, sans-serif;
  font-size: 1.3rem;
  font-weight: 300;
  line-height: 1.5rem;
  margin-right: 1rem;
}

.amp-tab {
  position: absolute;
  bottom: 0;
  right: 100%;
  border: none;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 20px 60px -2px rgba(27, 33, 58, 0.8);
  background-color: #32363d;
  cursor: pointer;
}

.amp-tab__icon {
  width: 30px;
  height: 30px;
  fill: #fa4238;
}

.amp-tab:active,
.amp-tab:focus {
  outline: none;
}

.amp-form {
  position: relative;
  padding: 20px;
  display: flex;
  flex-direction: column;
  overflow: scroll;
  flex-shrink: 1;
}

.amp-identity-item {
  margin-bottom: 1rem;
  display: flex;
}

.amp-identity-item__select {
  -webkit-appearance: none;
  -webkit-border-radius: 5px 0 0 5px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #607d8b;
  font-size: 1rem;
  background-color: #32363d;
  border: 1px solid #d4d7de;
  border-radius: 5px 0 0 5px;
  padding-left: 5px;
  transition: all 0.2s ease-in;
  cursor: pointer;
}

.amp-identity-item__select:after {
  content: "";
  position: absolute;
  width: 4px;
  height: 4px;
  background-color: red;
}

.amp-identity-item__select:hover {
  color: #fa4238;
  border-color: #fa4238;
}

.amp-identity-item__select:focus {
  outline: none;
}

.amp-identity-item__input {
  flex-grow: 1;
  padding: 0 0 0 6px;
  border: 1px solid #d4d7de;
  color: #607d8b;
  background-color: #fafcfd;
  border-radius: 0 5px 5px 0;
}

.amp-identity-item__input input,
.amp-identity-item__input select {
  position: relative;
  width: 100%;
  height: 100%;
  border: none;
  background-color: #fafcfd;
  font-size: 1rem;
  color: #607d8b;
}

.amp-identity-item__input input:focus,
.amp-identity-item__input select:focus {
  outline: none;
}

.amp-identity-item button {
  background-color: transparent;
  border: none;
  color: #d4d7de;
  font-size: 1.4rem;
  padding: 2px 6px;
  transition: all 0.2s ease-in;
  cursor: pointer;
}

.amp-identity-item button:hover {
  color: #fa4238;
}

#amp-input-uuid {
  margin-bottom: 0;
}

.amp-input-identity {
  margin-bottom: 1rem;
}

.amp-input-identity .input-block__inner {
  margin-bottom: 0;
}

.amp-input-identity__add {
  border: none;
  background-color: transparent;
  color: #607d8b;
  font-size: 1rem;
  transition: all 0.2s ease-in;
  cursor: pointer;
}

.amp-input-identity__add:hover {
  color: #fa4238;
}

.amp-input-identity__add:focus {
  border: none;
  outline: none;
  text-decoration: underline;
}

.input-block {
  margin-bottom: 1rem;
}

.input-block__heading {
  font-family: Source Sans Pro, sans-serif;
  color: #d4d7de;
  font-weight: 500;
  font-size: 1.4rem;
  margin-bottom: 1rem;
}

.input-block__inner {
  display: flex;
  margin-bottom: 1rem;
}

.input-block__label {
  display: inline-flex;
  margin-right: 1rem;
  margin-bottom: 0;
}

.input-block__button,
.input-block__label {
  height: 30px;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  color: #607d8b;
  background-color: #32363d;
}

.input-block__button {
  display: flex;
  border: 1px solid #d4d7de;
  border-radius: 5px;
  transition: all 0.2s ease-in;
  cursor: pointer;
}

.input-block__button--pill {
  border-radius: 5px 0 0 5px;
  border-right: none;
}

.input-block__button--inline {
  margin-left: 2px;
  background-color: transparent;
  border: none;
}

.input-block__button--inline:hover svg {
  fill: #fa4238;
}

.input-block__button--inline svg {
  width: 12px;
  height: 12px;
  fill: #fff;
  transition: all 0.2s ease-in;
}

.input-block__button:focus {
  outline: none;
  box-shadow: var(0 0 5px 3px rgba(96, 125, 139, 0.9));
}

.input-block__button:hover {
  color: #fa4238;
  border-color: #fa4238;
}

.input-block__button--spaced {
  margin-right: 1rem;
}

.input-block__input {
  flex-grow: 1;
  height: 30px;
  padding: 0 0 0 6px;
  border: 1px solid #d4d7de;
  font-size: 1rem;
  color: #607d8b;
  background-color: #fafcfd;
  border-radius: 5px;
  transition: all 0.2s ease-in;
}

.input-block__input--pill {
  border-radius: 0 5px 5px 0;
}

.input-block__input:focus {
  outline: none;
  box-shadow: 0 0 5px 3px rgba(96, 125, 139, 0.9);
}

.amp-debugger {
  position: relative;
  height: 300px;
  margin: 20px;
  flex-shrink: 0;
  background-color: #37474f;
  border-radius: 5px;
  box-shadow: inset 0 0 10px #32363d;
  overflow: scroll;
}

.amp-debugger__row {
  border-bottom: 1px solid #32363d;
  color: #d4d7de;
  max-height: 0;
  overflow: hidden;
  transition: 0.3s ease;
}

.amp-debugger__row a:hover {
  color: #fa4238;
}

.amp-debugger__message {
  display: block;
  padding: 10px;
  transition: all 0.2s ease-in;
}

.amp-debugger__message--error {
  color: #fc6065;
}

.amp-debugger__message--warn {
  color: #fcc360;
}

.amp-debugger__message--info {
  color: #4bdfaf;
}

.amp-debugger__data {
  padding: 0 10px 10px 30px;
}

@media print {
  .no-print {
    display: none !important;
  }
}

.amp {
  display: block !important;
  z-index: 10000;
}

/*# sourceMappingURL=/ui.css.map */
.amp {
  opacity: 0;
}
</style>

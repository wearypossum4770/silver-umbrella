import asyncio
from unittest import TestCase

import aiohttp
import pytest
from django.conf import settings
from django.core.cache import cache

from silver_umbrella.silver_umbrella_requests import requests
from users.views import registration

response_object = requests()
owasp_object = response_object.get("herokuapp")
# def test_memcache_functionality():
#     cache.get("foo")
#     cache.set("foo", "bar")
#     assert cache.get("foo") == "bar"
#     assert True == True


class TestOWASPHeaders(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.response = requests().get("herokuapp")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_herokuapp_header_http_strict_transport_security(self):
        owasp_object.get("HTTP Strict Transport Security")
        # "max-age=31536000 ; includeSubDomains"

    def test_herokuapp_header_x_frame_options(self):
        assert owasp_object.get("X-Frame-Options").lower() == "deny"

    def test_herokuapp_header_x_content_type_options(self):
        assert owasp_object.get("X-Content-Type-Options") == "nosniff"

    def test_herokuapp_header_content_security_policy(self):
        owasp_object.get("Content-Security-Policy")
        # == "default-src 'self' data:;"

    def test_herokuapp_header_x_permitted_cross_domain_policies(self):
        assert owasp_object.get("X-Permitted-Cross-Domain-Policies") == None

    def test_herokuapp_header_referrer_policy(self):
        assert owasp_object.get("Referrer-Policy") == "same-origin"
        # "no-referrer"

    def test_herokuapp_header_clear_site_data(self):
        owasp_object.get("Clear-Site-Data")
        # == ["cache","cookies","storage"]

    def test_herokuapp_header_cross_origin_embedder_policy(self):
        owasp_object.get("Cross-Origin-Embedder-Policy")
        # == "require-corp"

    def test_herokuapp_header_cross_origin_opener_policy(self):
        owasp_object.get("Cross-Origin-Opener-Policy")
        # =="same-origin"

    def test_herokuapp_header_cross_origin_resource_policy(self):
        owasp_object.get("Cross-Origin-Resource-Policy")
        # == "same-origin"

    def test_herokuapp_header_permissions_policy(self):
        owasp_object.get("Permissions-Policy")
        # == "accelerometer=()"

    def test_herokuapp_deprecated_header_public_key_pins(self):
        """
        Deprecated OWASP Response Header
        """
        assert owasp_object.get("Public-Key-Pins") == None

    def test_herokuapp_deprecated_header_x_xss_protection(self):
        """
        Deprecated OWASP Response Header
        """
        assert owasp_object.get("X-XSS-Protection") == None

    def test_herokuapp_decprecated_header_feature_policy(self):
        """
        Almost Deprecated OWASP Response Header
        """
        assert owasp_object.get("Feature-Policy") == None

    def test_herokuapp_decprecated_header_expect_ct(self):
        """
        Almost Deprecated OWASP Response Header
        """
        assert owasp_object.get("Expect-CT") == None


class TestSiteOperation(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.response = requests()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_homepage_page_connection(self):
        assert response_object.get("/") == 200

    def test_about_page_connection(self):
        assert response_object.get("/about/") == 200

    def test_registration_page_connection(self):
        assert response_object.get("/register/") == 200

    def test_password_reset_page_connection(self):
        assert response_object.get("/password-reset/") == 200

    def test_new_user_registration(self):
        """TODO"""
        assert response_object.get("http://127.0.0.1:8000/register/") == 200

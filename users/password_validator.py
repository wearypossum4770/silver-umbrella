owasp = {
    "configs": {
        "allowPassphrases": True,
        "maxLength": 128,
        "minLength": 10,
        "minPhraseLength": 20,
        "minOptionalTestsToPass":4,
    }
}


def config(*args, **kwargs):
    owasp["configs"]["allowPassphrases"] = allowPassphrases
    owasp["configs"]["maxLength"] = maxLength
    owasp["configs"]["minLength"] = minLength
    owasp["configs"]["minPhraseLength"] = minPhraseLength
    owasp["configs"]["minOptionalTestsToPass"] = minOptionalTestsToPass


config(owasp)
print(owasp)

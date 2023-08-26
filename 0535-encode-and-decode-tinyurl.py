class Codec:
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        shortUrl = "https://tinyurl.com/" + str(hash(longUrl))
        self.urls[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        longUrl = self.urls[shortUrl]
        del self.urls[shortUrl]
        return longUrl


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

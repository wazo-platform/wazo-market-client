# wazo-market-client
A python client for apps.wazo.community

## Usage

### Creating a client

```python
from wazo_market_client import Client
c = Client()
```

### Listing available plugins

```python
c.plugins.list()
```

## Debian package

Follow the following steps to build a debian package for wazo-market-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/wazo-market-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```


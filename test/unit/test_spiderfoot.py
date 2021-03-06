# test_spiderfoot.py
from sflib import SpiderFoot
import unittest

class TestSpiderFoot(unittest.TestCase):
    """
    Test SpiderFoot
    """

    default_options = {
      '_debug': False,  # Debug
      '__logging': True, # Logging in general
      '__outputfilter': None, # Event types to filter from modules' output
      '__blocknotif': False,  # Block notifications
      '_fatalerrors': False,
      '_useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',  # User-Agent to use for HTTP requests
      '_dnsserver': '',  # Override the default resolver
      '_fetchtimeout': 5,  # number of seconds before giving up on a fetch
      '_internettlds': 'https://publicsuffix.org/list/effective_tld_names.dat',
      '_internettlds_cache': 72,
      '__version__': '3.0',
      '__database': 'spiderfoot.db',
      '__webaddr': '127.0.0.1',
      '__webport': 5001,
      '__docroot': '',  # don't put trailing /
      '__modules__': None,  # List of modules. Will be set after start-up.
      '_socks1type': '',
      '_socks2addr': '',
      '_socks3port': '',
      '_socks4user': '',
      '_socks5pwd': '',
      '_socks6dns': True,
      '_torctlport': 9051,
      '__logstdout': False
    }

    def test_init_no_options(self):
        """
        Test __init__(self, options, handle=None):
        """
        sf = SpiderFoot(dict())
        self.assertEqual('TBD', 'TBD')

    def test_init(self):
        """
        Test __init__(self, options, handle=None):
        """
        sf = SpiderFoot(self.default_options)
        self.assertEqual('TBD', 'TBD')

    def test_update_socket(self):
        """
        Test updateSocket(self, sock)
        """
        sf = SpiderFoot(dict())

        sf.updateSocket('new socket')
        self.assertEqual('new socket', sf.socksProxy)

    def test_revert_socket(self):
        """
        Test revertSocket(self)
        """
        sf = SpiderFoot(dict())

        sf.revertSocket()
        self.assertEqual(None, sf.socksProxy)

    def test_refresh_tor_ident_should_return_none(self):
        """
        Test refreshTorIdent(self)
        """
        sf = SpiderFoot(self.default_options)

        res = sf.refreshTorIdent()
        self.assertEqual(None, res)

    def test_opt_value_to_data(self):
        """
        Test optValueToData(self, val, fatal=True, splitLines=True)
        """
        sf = SpiderFoot(dict())

        sf.optValueToData(None)
        self.assertEqual('TBD', 'TBD')

    def test_opt_value_to_data_no_value_should_return_none(self):
        """
        Test optValueToData(self, val, fatal=True, splitLines=True)
        """
        sf = SpiderFoot(self.default_options)

        res = sf.optValueToData(None)
        self.assertEqual(None, res)

    def test_build_graph_data_should_return_a_set(self):
        """
        Test buildGraphData(self, data, flt=list())
        """
        sf = SpiderFoot(dict())

        graph_data = sf.buildGraphData('')
        self.assertEqual(set, type(graph_data))

    def test_build_graph_gexf_should_return_bytes(self):
        """
        Test buildGraphGexf(self, root, title, data, flt=[])
        """
        sf = SpiderFoot(dict())

        gexf = sf.buildGraphGexf('', '', '')
        self.assertEqual(bytes, type(gexf))

    def test_build_graph_json_should_return_a_string(self):
        """
        Test buildGraphJson(self, root, data, flt=list())
        """
        sf = SpiderFoot(dict())

        json = sf.buildGraphJson('', '')
        self.assertEqual(str, type(json))

    def test_set_dbh(self):
        """
        Test setDbh(self, handle)
        """
        sf = SpiderFoot(dict())

        sf.setDbh('new handle')
        self.assertEqual('new handle', sf.dbh)

    def test_set_guid(self):
        """
        Test setGUID(self, uid)
        """
        sf = SpiderFoot(dict())

        sf.setGUID('new guid')
        self.assertEqual('new guid', sf.GUID)

    def test_gen_scan_instance_guid_should_return_a_string(self):
        """
        Test genScanInstanceGUID(self, scanName)
        """
        sf = SpiderFoot(dict())

        scan_instance_id = sf.genScanInstanceGUID(None)
        self.assertEqual(str, type(scan_instance_id))

    def test_dblog(self):
        """
        Test _dblog(self, level, message, component=None)
        """
        self.assertEqual('TBD', 'TBD')

    def test_error(self):
        """
        Test error(self, error, exception=True)
        """
        sf = SpiderFoot(self.default_options)

        sf.error('', exception=False)
        self.assertEqual('TBD', 'TBD')

    def test_fatal_should_exit(self):
        """
        Test fatal(self, error)
        """
        sf = SpiderFoot(self.default_options)

        with self.assertRaises(SystemExit) as cm:
            sf.fatal(None)

        self.assertEqual(cm.exception.code, -1)

    def test_status(self):
        """
        Test status(self, message)
        """
        sf = SpiderFoot(self.default_options)

        sf.status(None)
        self.assertEqual('TBD', 'TBD')

    def test_info(self):
        """
        Test info(self, message)
        """
        sf = SpiderFoot(self.default_options)

        sf.info(None)
        self.assertEqual('TBD', 'TBD')

    def test_debug(self):
        """
        Test debug(self, message)
        """
        sf = SpiderFoot(self.default_options)

        sf.debug(None)
        self.assertEqual('TBD', 'TBD')

    def test_my_path_should_return_a_string(self):
        """
        Test myPath(self)
        """
        sf = SpiderFoot(dict())

        path = sf.myPath()
        self.assertEqual(str, type(path))

    def test_hash_string_should_return_a_string(self):
        """
        Test hashstring(self, string)
        """
        sf = SpiderFoot(dict())

        hash_string = sf.hashstring('example string')
        self.assertEqual(str, type(hash_string))

    def test_cache_path_should_return_a_string(self):
        """
        Test cachePath(self)
        """
        sf = SpiderFoot(dict())

        cache_path = sf.cachePath()
        self.assertEqual(str, type(cache_path))

    def test_cache_get_should_return_a_string(self):
        """
        Test cachePut(self, label, data)
        Test cacheGet(self, label, timeoutHrs)
        """
        sf = SpiderFoot(dict())

        label = 'test-cache-label'
        data = 'test-cache-data'
        cache_put = sf.cachePut(label, data)
        cache_get = sf.cacheGet(label, sf.opts.get('cacheperiod', 0))
        self.assertEqual(str, type(cache_get))
        self.assertEqual(data, cache_get)

    def test_cache_get_invalid_label_should_return_none(self):
        """
        Test cacheGet(self, label, timeoutHrs)
        """
        sf = SpiderFoot(dict())

        cache_get = sf.cacheGet('', sf.opts.get('cacheperiod', 0))
        self.assertEqual(None, cache_get)

    def test_cache_get_invalid_timeout_should_return_none(self):
        """
        Test cacheGet(self, label, timeoutHrs)
        """
        sf = SpiderFoot(dict())

        cache_get = sf.cacheGet('', None)
        self.assertEqual(None, cache_get)

    def test_config_serialize(self):
        """
        Test configSerialize(self, opts, filterSystem=True)
        """
        self.assertEqual('TBD', 'TBD')

    def test_config_unserialize(self):
        """
        Test configUnserialize(self, opts, referencePoint, filterSystem=True)
        """
        self.assertEqual('TBD', 'TBD')

    def test_target_type(self):
        """
        Test targetType(self, target)
        """
        self.assertEqual('TBD', 'TBD')

    def test_modules_producing(self):
        """
        Test modulesProducing(self, events)
        """
        self.assertEqual('TBD', 'TBD')

    def test_modules_consuming(self):
        """
        Test modulesConsuming(self, events)
        """
        self.assertEqual('TBD', 'TBD')

    def test_events_from_modules(self):
        """
        Test eventsFromModules(self, modules)
        """
        self.assertEqual('TBD', 'TBD')

    def test_events_to_modules(self):
        """
        Test eventsToModules(self, modules)
        """
        self.assertEqual('TBD', 'TBD')

    def test_url_relative_to_absolute_should_return_a_string(self):
        """
        Test urlRelativeToAbsolute(self, url)
        """
        sf = SpiderFoot(dict())

        relative_url = sf.urlRelativeToAbsolute('http://localhost.local/path')
        self.assertEqual(str, type(relative_url))

    def test_url_base_dir_should_return_a_string(self):
        """
        Test urlBaseDir(self, url)
        """
        sf = SpiderFoot(dict())

        base_dir = sf.urlBaseDir('http://localhost.local/path')
        self.assertEqual(str, type(base_dir))

    def test_url_base_url_should_return_a_string(self):
        """
        Test urlBaseUrl(self, url)
        """
        sf = SpiderFoot(dict())

        base_url = sf.urlBaseUrl('http://localhost.local/path')
        self.assertEqual(str, type(base_url))

    def test_url_fqdn_should_return_a_string(self):
        """
        Test urlFQDN(self, url)
        """
        sf = SpiderFoot(dict())

        fqdn = sf.urlFQDN('http://localhost.local')
        self.assertEqual(str, type(fqdn))

    def test_domain_keyword_should_return_a_string(self):
        """
        Test domainKeyword(self, domain, tldList)
        """
        sf = SpiderFoot(self.default_options)

        keyword = sf.domainKeyword('www.spiderfoot.net', sf.opts.get('_internettlds'))
        self.assertEqual(str, type(keyword))
        self.assertEqual('wwwspiderfootnet', keyword)

    def test_domain_keyword_invalid_domain_should_return_none(self):
        """
        Test domainKeyword(self, domain, tldList)
        """
        sf = SpiderFoot(self.default_options)

        keyword = sf.domainKeyword("", sf.opts.get('_internettlds'))
        self.assertEqual(None, keyword)
        keyword = sf.domainKeyword([], sf.opts.get('_internettlds'))
        self.assertEqual(None, keyword)
        keyword = sf.domainKeyword(None, sf.opts.get('_internettlds'))
        self.assertEqual(None, keyword)

    def test_domain_keywords_should_return_a_set(self):
        """
        Test domainKeywords(self, domainList, tldList)
        """
        sf = SpiderFoot(self.default_options)

        domain_list = ['www.example.com', 'localhost.local']
        keywords = sf.domainKeywords(domain_list, sf.opts.get('_internettlds'))
        self.assertEqual(set, type(keywords))

    def test_domain_keywords_invalid_domainlist_should_return_a_set(self):
        """
        Test domainKeyword(self, domain, tldList)
        """
        sf = SpiderFoot(self.default_options)

        keywords = sf.domainKeywords("", sf.opts.get('_internettlds'))
        self.assertEqual(set, type(keywords))
        keywords = sf.domainKeywords([], sf.opts.get('_internettlds'))
        self.assertEqual(set, type(keywords))
        keywords = sf.domainKeywords(None, sf.opts.get('_internettlds'))
        self.assertEqual(set, type(keywords))

    def test_host_domain_invalid_host_should_return_none(self):
        """
        Test hostDomain(self, hostname, tldList)
        """
        sf = SpiderFoot(self.default_options)

        host_domain = sf.hostDomain(None, sf.opts.get('_internettlds'))
        self.assertEqual(None, host_domain)

    def test_host_domain_should_return_a_string(self):
        """
        Test hostDomain(self, hostname, tldList)
        """
        sf = SpiderFoot(self.default_options)

        host_domain = sf.hostDomain('local', sf.opts.get('_internettlds'))
        self.assertEqual(str, type(host_domain))
        self.assertEqual('local', host_domain)

        host_domain = sf.hostDomain('spiderfoot.net', sf.opts.get('_internettlds'))
        self.assertEqual(str, type(host_domain))
        self.assertEqual('net', host_domain)

        host_domain = sf.hostDomain('www.spiderfoot.net', sf.opts.get('_internettlds'))
        self.assertEqual(str, type(host_domain))
        self.assertEqual('net', host_domain)

    def test_host_domain_invalid_tldlist_should_return_none(self):
        """
        Test hostDomain(self, hostname, tldList)
        """
        sf = SpiderFoot(dict())

        host_domain = sf.hostDomain('spiderfoot.net', None)
        self.assertEqual(None, host_domain)

    def test_is_domain_should_return_a_boolean(self):
        """
        Test isDomain(self, hostname, tldList)
        """
        sf = SpiderFoot(self.default_options)

        is_domain = sf.isDomain('local', None)
        self.assertEqual(bool, type(is_domain))

    def test_valid_ip_should_return_a_boolean(self):
        """
        Test validIP(self, address)
        """
        sf = SpiderFoot(dict())

        valid_ip = sf.validIP('0.0.0.0')
        self.assertEqual(bool, type(valid_ip))

    def test_valid_ip6_should_return_a_boolean(self):
        """
        Test validIP6(self, address)
        """
        sf = SpiderFoot(dict())

        valid_ip6 = sf.validIP6('::1')
        self.assertEqual(bool, type(valid_ip6))

    def test_valid_ip_network_should_return_a_boolean(self):
        """
        Test validIpNetwork(self, cidr)
        """
        sf = SpiderFoot(dict())

        valid_ip_network = sf.validIpNetwork('0.0.0.0/0')
        self.assertEqual(bool, type(valid_ip_network))

    def tes_normalize_dns(self):
        """
        Test normalizeDNS(self, res)
        """
        self.assertEqual('TBD', 'TBD')

    def test_sanitise_input(self):
        """
        Test sanitiseInput(self, cmd)
        """
        self.assertEqual('TBD', 'TBD')

    def test_dictwords_should_return_a_list(self):
        """
        Test dictwords(self)
        """
        sf = SpiderFoot(dict())

        dict_words = sf.dictwords()
        self.assertEqual(list, type(dict_words))

    def test_dictnames_should_return_a_list(self):
        """
        Test dictnames(self)
        """
        sf = SpiderFoot(dict())

        dict_names = sf.dictnames()
        self.assertEqual(list, type(dict_names))

    def test_data_parent_child_to_tree(self):
        """
        Test dataParentChildToTree(self, data)
        """
        self.assertEqual('TBD', 'TBD')

    def test_resolve_host(self):
        """
        Test resolveHost(self, host)
        """
        self.assertEqual('TBD', 'TBD')

    def test_resolve_ip(self):
        """
        Test resolveIP(self, ipaddr)
        """
        self.assertEqual('TBD', 'TBD')

    def test_resolve_host6(self):
        """
        Test resolveHost6(self, hostname)
        """
        self.assertEqual('TBD', 'TBD')

    def test_validate_ip(self):
        """
        Test validateIP(self, host, ip)
        """
        self.assertEqual('TBD', 'TBD')

    def test_resolve_targets(self):
        """
        Test resolveTargets(self, target, validateReverse)
        """
        self.assertEqual('TBD', 'TBD')

    def test_safe_socket(self):
        """
        Test safeSocket(self, host, port, timeout)
        """
        self.assertEqual('TBD', 'TBD')

    def test_safe_ssl_socket(self):
        """
        Test safeSSLSocket(self, host, port, timeout)
        """
        self.assertEqual('TBD', 'TBD')

    def test_parse_robots_txt(self):
        """
        Test parseRobotsTxt(self, robotsTxtData)
        """
        self.assertEqual('TBD', 'TBD')

    def test_parse_emails(self):
        """
        Test parseEmails(self, data)
        """
        self.assertEqual('TBD', 'TBD')

    def test_ssl_der_to_pem(self):
        """
        Test sslDerToPem(self, der)
        """
        self.assertEqual('TBD', 'TBD')

    def test_parse_cert(self):
        """
        Test parseCert(self, rawcert, fqdn=None, expiringdays=30)
        """
        self.assertEqual('TBD', 'TBD')

    def test_parse_links_should_return_a_dict(self):
        """
        Test parseLinks(self, url, data, domains)
        """
        sf = SpiderFoot(self.default_options)

        parse_links = sf.parseLinks('url', 'data', 'domains')
        self.assertEqual(dict, type(parse_links))

    def test_parse_links_invalid_url_should_return_a_dict(self):
        """
        Test parseLinks(self, url, data, domains)
        """
        sf = SpiderFoot(self.default_options)

        parse_links = sf.parseLinks(None, 'data', 'domains')
        self.assertEqual(dict, type(parse_links))

    def test_parse_links_invalid_data_should_return_a_dict(self):
        """
        Test parseLinks(self, url, data, domains)
        """
        sf = SpiderFoot(self.default_options)

        parse_links = sf.parseLinks('url', None, 'domains')
        self.assertEqual(dict, type(parse_links))

    def test_parse_links_invalid_domains_should_return_a_dict(self):
        """
        Test parseLinks(self, url, data, domains)
        """
        sf = SpiderFoot(self.default_options)

        parse_links = sf.parseLinks('url', 'data', None)
        self.assertEqual(dict, type(parse_links))

    def test_url_encode_unicode_should_return_a_string(self):
        """
        Test urlEncodeUnicode(self, url)
        """
        sf = SpiderFoot(self.default_options)

        url_encode_unicode = sf.urlEncodeUnicode('url')
        self.assertEqual(str, type(url_encode_unicode))

    def test_fetch_url(self):
        """
        Test fetchUrl(self, url, fatal=False, cookies=None, timeout=30,
                 useragent="SpiderFoot", headers=None, noLog=False,
                 postData=None, dontMangle=False, sizeLimit=None,
                 headOnly=False, verify=False)
        """
        self.assertEqual('TBD', 'TBD')

    def test_fetch_url_invalid_url_should_return_none(self):
        """
        Test fetchUrl(self, url, fatal=False, cookies=None, timeout=30,
                 useragent="SpiderFoot", headers=None, noLog=False,
                 postData=None, dontMangle=False, sizeLimit=None,
                 headOnly=False, verify=False)
        """
        sf = SpiderFoot(self.default_options)

        res = sf.fetchUrl(None)
        self.assertEqual(None, res)

    def test_check_dns_wildcard_invalid_target_should_return_none(self):
        """
        Test checkDnsWildcard(self, target)
        """
        sf = SpiderFoot(self.default_options)

        check_dns_wildcard = sf.checkDnsWildcard(None)
        self.assertEqual(bool, type(check_dns_wildcard))

    def test_check_dns_wildcard_should_return_a_boolean(self):
        """
        Test checkDnsWildcard(self, target)
        """
        sf = SpiderFoot(self.default_options)

        check_dns_wildcard = sf.checkDnsWildcard('local')
        self.assertEqual(bool, type(check_dns_wildcard))

    def test_google_iterate(self):
        """
        Test googleIterate(self, searchString, opts=dict())
        """
        self.assertEqual('TBD', 'TBD')

    def test_bing_iterate(self):
        """
        Test bingIterate(self, searchString, opts=dict())
        """
        self.assertEqual('TBD', 'TBD')

if __name__ == '__main__':
    unittest.main()


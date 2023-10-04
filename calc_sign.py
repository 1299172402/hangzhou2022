import execjs
import json

# define the JavaScript code
js_code = """
function calcsign(t){
    function e(t, e) {
        return t << e | t >>> 32 - e
    }
    function r(t, e) {
        var r, n, o, i, a;
        return o = 2147483648 & t,
        i = 2147483648 & e,
        r = 1073741824 & t,
        n = 1073741824 & e,
        a = (1073741823 & t) + (1073741823 & e),
        r & n ? 2147483648 ^ a ^ o ^ i : r | n ? 1073741824 & a ? 3221225472 ^ a ^ o ^ i : 1073741824 ^ a ^ o ^ i : a ^ o ^ i
    }
    function n(t, e, r) {
        return t & e | ~t & r
    }
    function o(t, e, r) {
        return t & r | e & ~r
    }
    function i(t, e, r) {
        return t ^ e ^ r
    }
    function a(t, e, r) {
        return e ^ (t | ~r)
    }
    function c(t, o, i, a, c, u, s) {
        return t = r(t, r(r(n(o, i, a), c), s)),
        r(e(t, u), o)
    }
    function u(t, n, i, a, c, u, s) {
        return t = r(t, r(r(o(n, i, a), c), s)),
        r(e(t, u), n)
    }
    function s(t, n, o, a, c, u, s) {
        return t = r(t, r(r(i(n, o, a), c), s)),
        r(e(t, u), n)
    }
    function l(t, n, o, i, c, u, s) {
        return t = r(t, r(r(a(n, o, i), c), s)),
        r(e(t, u), n)
    }
    function p(t) {
        var e, r = t.length, n = r + 8, o = (n - n % 64) / 64, i = 16 * (o + 1), a = Array(i - 1), c = 0, u = 0;
        while (u < r)
            e = (u - u % 4) / 4,
            c = u % 4 * 8,
            a[e] = a[e] | t.charCodeAt(u) << c,
            u++;
        return e = (u - u % 4) / 4,
        c = u % 4 * 8,
        a[e] = a[e] | 128 << c,
        a[i - 2] = r << 3,
        a[i - 1] = r >>> 29,
        a
    }
    function h(t) {
        var e, r, n = "", o = "";
        for (r = 0; r <= 3; r++)
            e = t >>> 8 * r & 255,
            o = "0".concat(e.toString(16)),
            n += o.substr(o.length - 2, 2);
        return n
    }
    function f(t) {
        /* t = t.replace(/\r\n/g, "\n"); */
        for (var e = "", r = 0; r < t.length; r++) {
            var n = t.charCodeAt(r);
            n < 128 ? e += String.fromCharCode(n) : n > 127 && n < 2048 ? (e += String.fromCharCode(n >> 6 | 192),
            e += String.fromCharCode(63 & n | 128)) : (e += String.fromCharCode(n >> 12 | 224),
            e += String.fromCharCode(n >> 6 & 63 | 128),
            e += String.fromCharCode(63 & n | 128))
        }
        return e
    }
    var d, v, y, g, m, _, w, b, x, O = [], L = 7, j = 12, E = 17, S = 22, k = 5, P = 9, C = 14, I = 20, N = 4, T = 11, G = 16, F = 23, A = 6, D = 10, M = 15, B = 21;
    for (t = f(t),
    O = p(t),
    _ = 1732584193,
    w = 4023233417,
    b = 2562383102,
    x = 271733878,
    d = 0; d < O.length; d += 16)
        v = _,
        y = w,
        g = b,
        m = x,
        _ = c(_, w, b, x, O[d + 0], L, 3614090360),
        x = c(x, _, w, b, O[d + 1], j, 3905402710),
        b = c(b, x, _, w, O[d + 2], E, 606105819),
        w = c(w, b, x, _, O[d + 3], S, 3250441966),
        _ = c(_, w, b, x, O[d + 4], L, 4118548399),
        x = c(x, _, w, b, O[d + 5], j, 1200080426),
        b = c(b, x, _, w, O[d + 6], E, 2821735955),
        w = c(w, b, x, _, O[d + 7], S, 4249261313),
        _ = c(_, w, b, x, O[d + 8], L, 1770035416),
        x = c(x, _, w, b, O[d + 9], j, 2336552879),
        b = c(b, x, _, w, O[d + 10], E, 4294925233),
        w = c(w, b, x, _, O[d + 11], S, 2304563134),
        _ = c(_, w, b, x, O[d + 12], L, 1804603682),
        x = c(x, _, w, b, O[d + 13], j, 4254626195),
        b = c(b, x, _, w, O[d + 14], E, 2792965006),
        w = c(w, b, x, _, O[d + 15], S, 1236535329),
        _ = u(_, w, b, x, O[d + 1], k, 4129170786),
        x = u(x, _, w, b, O[d + 6], P, 3225465664),
        b = u(b, x, _, w, O[d + 11], C, 643717713),
        w = u(w, b, x, _, O[d + 0], I, 3921069994),
        _ = u(_, w, b, x, O[d + 5], k, 3593408605),
        x = u(x, _, w, b, O[d + 10], P, 38016083),
        b = u(b, x, _, w, O[d + 15], C, 3634488961),
        w = u(w, b, x, _, O[d + 4], I, 3889429448),
        _ = u(_, w, b, x, O[d + 9], k, 568446438),
        x = u(x, _, w, b, O[d + 14], P, 3275163606),
        b = u(b, x, _, w, O[d + 3], C, 4107603335),
        w = u(w, b, x, _, O[d + 8], I, 1163531501),
        _ = u(_, w, b, x, O[d + 13], k, 2850285829),
        x = u(x, _, w, b, O[d + 2], P, 4243563512),
        b = u(b, x, _, w, O[d + 7], C, 1735328473),
        w = u(w, b, x, _, O[d + 12], I, 2368359562),
        _ = s(_, w, b, x, O[d + 5], N, 4294588738),
        x = s(x, _, w, b, O[d + 8], T, 2272392833),
        b = s(b, x, _, w, O[d + 11], G, 1839030562),
        w = s(w, b, x, _, O[d + 14], F, 4259657740),
        _ = s(_, w, b, x, O[d + 1], N, 2763975236),
        x = s(x, _, w, b, O[d + 4], T, 1272893353),
        b = s(b, x, _, w, O[d + 7], G, 4139469664),
        w = s(w, b, x, _, O[d + 10], F, 3200236656),
        _ = s(_, w, b, x, O[d + 13], N, 681279174),
        x = s(x, _, w, b, O[d + 0], T, 3936430074),
        b = s(b, x, _, w, O[d + 3], G, 3572445317),
        w = s(w, b, x, _, O[d + 6], F, 76029189),
        _ = s(_, w, b, x, O[d + 9], N, 3654602809),
        x = s(x, _, w, b, O[d + 12], T, 3873151461),
        b = s(b, x, _, w, O[d + 15], G, 530742520),
        w = s(w, b, x, _, O[d + 2], F, 3299628645),
        _ = l(_, w, b, x, O[d + 0], A, 4096336452),
        x = l(x, _, w, b, O[d + 7], D, 1126891415),
        b = l(b, x, _, w, O[d + 14], M, 2878612391),
        w = l(w, b, x, _, O[d + 5], B, 4237533241),
        _ = l(_, w, b, x, O[d + 12], A, 1700485571),
        x = l(x, _, w, b, O[d + 3], D, 2399980690),
        b = l(b, x, _, w, O[d + 10], M, 4293915773),
        w = l(w, b, x, _, O[d + 1], B, 2240044497),
        _ = l(_, w, b, x, O[d + 8], A, 1873313359),
        x = l(x, _, w, b, O[d + 15], D, 4264355552),
        b = l(b, x, _, w, O[d + 6], M, 2734768916),
        w = l(w, b, x, _, O[d + 13], B, 1309151649),
        _ = l(_, w, b, x, O[d + 4], A, 4149444226),
        x = l(x, _, w, b, O[d + 11], D, 3174756917),
        b = l(b, x, _, w, O[d + 2], M, 718787259),
        w = l(w, b, x, _, O[d + 9], B, 3951481745),
        _ = r(_, v),
        w = r(w, y),
        b = r(b, g),
        x = r(x, m);
    return (h(_) + h(w) + h(b) + h(x)).toLowerCase()
}
"""

# create a JavaScript context
context = execjs.compile(js_code)

def calc_sign(params, timestamp):
    # convert the params to a string
    for key in params:
        if params[key] == True:
            params[key] = 'true'
        elif params[key] == False:
            params[key] = 'false'
        else:
            params[key] = str(params[key]).replace('%2C', ',')
    params = {k: params[k] for k in sorted(params)}

    # add the timestamp
    params["timestamp"] = str(timestamp)
    data = json.dumps(params, separators=(',', ':'))

    # call the JavaScript function
    result = context.call("calcsign", data)
    return result

def params2json(params):
    data = {}
    for pair in params.split('&'):
        key, value = pair.split('=')
        data[key] = value
    return data

if __name__ == '__main__':
    p = "sortType=2&page=1&pageSize=36&venueIds=2056005017481%2C2044008017481%2C2057005017481%2C2044007017481%2C2044006017481%2C2051003017481%2C2040004017481%2C2044005017481%2C2056004017481%2C2055005017481%2C2056003017481%2C2057004017481%2C2058002017481%2C2052003017481%2C2055004017481%2C2058001017481%2C2046005017481%2C2056002017481%2C2057003017481%2C2057002017481%2C2041002017481%2C2051002017481%2C2044004017481%2C2044003017481%2C2052002017481%2C2055003017481%2C2057001017481%2C2044002017481%2C2056001017481%2C2040003017481%2C2020003017481%2C2030004017481%2C2036002017481%2C2034004017481%2C2029003017481%2C2037002017481%2C2034003017481%2C2025005017481%2C2016004017481%2C1085002017481&langType=1"
    print(calc_sign(params2json(p), 1696397513468))

    data = '{"langType":"1","page":"1","pageSize":"36","sortType":"2","venueIds":"2056005017481,2044008017481,2057005017481,2044007017481,2044006017481,2051003017481,2040004017481,2044005017481,2056004017481,2055005017481,2056003017481,2057004017481,2058002017481,2052003017481,2055004017481,2058001017481,2046005017481,2056002017481,2057003017481,2057002017481,2041002017481,2051002017481,2044004017481,2044003017481,2052002017481,2055003017481,2057001017481,2044002017481,2056001017481,2040003017481,2020003017481,2030004017481,2036002017481,2034004017481,2029003017481,2037002017481,2034003017481,2025005017481,2016004017481,1085002017481","timestamp":"1696397513468"}'
    print(context.call("calcsign", data))

    p = "projectId=216758012&langType=1"
    print(calc_sign(params2json(p), 1696399309889))


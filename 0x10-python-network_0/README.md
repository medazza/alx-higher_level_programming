# 0x10. Python - Network #0

## Table of Contents
- [What is a URL?](#what-is-a-url)
- [What is HTTP?](#what-is-http)
- [How to Read a URL](#how-to-read-a-url)
- [The Scheme for an HTTP URL](#the-scheme-for-an-http-url)
- [What is a Domain Name?](#what-is-a-domain-name)
- [What is a Sub-Domain?](#what-is-a-sub-domain)
- [How to Define a Port Number in a URL](#how-to-define-a-port-number-in-a-url)
- [What is a Query String?](#what-is-a-query-string)
- [What is an HTTP Request?](#what-is-an-http-request)
- [What is an HTTP Response?](#what-is-an-http-response)
- [What are HTTP Headers?](#what-are-http-headers)
- [What is the HTTP Message Body?](#what-is-the-http-message-body)
- [What is an HTTP Request Method?](#what-is-an-http-request-method)
- [What is an HTTP Response Status Code?](#what-is-an-http-response-status-code)
- [What is an HTTP Cookie?](#what-is-an-http-cookie)
- [How to Make a Request with cURL](#how-to-make-a-request-with-curl)
- [What Happens When You Type google.com in Your Browser (Application Level)](#what-happens-when-you-type-googlecom-in-your-browser-application-level)

## What is a URL?

A **Uniform Resource Locator (URL)** is a reference or address used to access resources on the internet. It specifies the means to access a resource, the network location, and the path to the resource.

## What is HTTP?

**HTTP (Hypertext Transfer Protocol)** is an application-layer protocol used for transmitting hypermedia documents, such as HTML. It is the foundation of data communication on the World Wide Web.

## How to Read a URL

A URL consists of several components:
- **Scheme:** Specifies the protocol used (e.g., `http`, `https`).
- **Domain:** Identifies the server's address.
- **Port:** Specifies the port number for the server (optional).
- **Path:** Specifies the location of the resource on the server.
- **Query String:** Provides additional parameters for the resource.

Example: `https://www.example.com:8080/path/to/resource?param1=value1&param2=value2`

## The Scheme for an HTTP URL

The scheme for an HTTP URL is typically `http` or `https`. `http` is the standard protocol, while `https` is a secure version that uses encryption.

## What is a Domain Name?

A **domain name** is a human-readable label assigned to an IP address on the internet. It provides a way to access resources without remembering numeric IP addresses.

## What is a Sub-Domain?

A **sub-domain** is a domain that is part of a larger domain. For example, in `blog.example.com`, "blog" is a sub-domain of "example.com."

## How to Define a Port Number in a URL

A port number is specified after the domain, separated by a colon. Example: `http://example.com:8080`.

## What is a Query String?

A **query string** is a part of the URL that follows the path and is used to pass parameters to the resource. Example: `?param1=value1&param2=value2`.

## What is an HTTP Request?

An **HTTP request** is a message sent by a client to a server, requesting a specific action.

## What is an HTTP Response?

An **HTTP response** is a message sent by a server to a client, providing the result of the requested action.

## What are HTTP Headers?

**HTTP headers** are metadata elements transmitted in both requests and responses. They provide information about the communication.

## What is the HTTP Message Body?

The **HTTP message body** carries the payload of the message, such as the content of a file being sent.

## What is an HTTP Request Method?

The **HTTP request method** specifies the desired action to be performed on the identified resource. Common methods include GET, POST, and PUT.

## What is an HTTP Response Status Code?

An **HTTP response status code** indicates the success, failure, or redirection of an HTTP request. Examples include 200 OK, 404 Not Found, and 500 Internal Server Error.

## What is an HTTP Cookie?

An **HTTP cookie** is a small piece of data sent from a server and stored on the client's device. It maintains session information between the client and server.

## How to Make a Request with cURL

**cURL** is a command-line tool for making HTTP requests. Example:
```bash
curl -X GET https://www.example.com
```

## What Happens When You Type google.com in Your Browser (Application Level)

When you type `google.com` in your browser:
1. The browser checks its cache for a DNS record to find the corresponding IP address.
2. If not found, the browser sends a DNS request to resolve the domain.
3. Once resolved, the browser establishes a TCP connection to the server.
4. The browser sends an HTTP request to the server.
5. The server processes the request and sends back an HTTP response.
6. The browser renders the response and displays the page.

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17
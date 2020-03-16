<a name="1.0.10"></a>
## [1.0.10](https://bitbucket.org/factoryconcepts/critical-path-mapping/compare/v1.0.9...v1.0.10) (2015-10-13)


### Bug Fixes

* resolve additional IE-specific comment errors ([809ec79](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/809ec79))
* resolve font issues in header ([52536d4](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/52536d4))

### Features

* force lowercase in email address during authentication ([19c736d](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/19c736d))
* force lowercase on email addresses in User model ([075860b](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/075860b))
* prepare for migration to criticalpathmapping.com domain ([93468d6](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/93468d6))
* remove dependance on Google Fonts CDN ([b6c60e1](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/b6c60e1))
* switch password hashing to PBKDF2 at 2000000 iterations for more gooder security ([a958caa](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/a958caa))



<a name="1.0.9"></a>
## [1.0.9](https://bitbucket.org/factoryconcepts/critical-path-mapping/compare/v1.0.8...v1.0.9) (2015-09-14)


### Bug Fixes

* **operations:** change operation description to TextField ([beb3cf1](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/beb3cf1))
* IE DOM selection not working properly in charts ([d1cbb56](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/d1cbb56))
* comment out all console logging output and add space to @todo comments, which we ([2a4abbf](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/2a4abbf))

### Features

* update oCanvas to v2.8.1 ([dab1465](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/dab1465))



<a name="1.0.8"></a>
## [1.0.8](https://bitbucket.org/factoryconcepts/critical-path-mapping/compare/v1.0.7...v1.0.8) (2015-08-24)


### Bug Fixes

* **admin:** superadmin user creation assigned to incorrect form ([b1fb0b4](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/b1fb0b4))
* **operations:** cell templates contain appropriate spaces between elements ([1354bc9](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/1354bc9))
* add custom angular-ui-grid build to resolve pipeline static collection failure ([d15e52b](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/d15e52b))

### Features

* update all frontend libraries ([40c1b27](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/40c1b27))
* use bower to manage frontend dependencies ([986961c](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/986961c))
* **operations:** set error on rows if end date is before or equal to start date ([9c1d5f2](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/9c1d5f2))



<a name="1.0.7"></a>
## [1.0.7](https://bitbucket.org/factoryconcepts/critical-path-mapping/compare/v1.0.6...v1.0.7) (2015-08-14)


### Bug Fixes

* **admin:** filter operation methods by company ([27d7840](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/27d7840))
* **admin:** filter parts by company ([9778a79](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/9778a79))
* **admin:** filter users by company ([de6845c](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/de6845c))
* **admin:** filter work periods by company ([31fb6a4](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/31fb6a4))
* **admin:** resolve filtering of operation methods ([e6a39a7](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/e6a39a7))
* **data:** remove extraneous test accounts from production fixtures ([ef6851c](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/ef6851c))
* **fixtures:** update test user passwords ([82a181b](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/82a181b))
* change admin labels in main menu ([56f0bce](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/56f0bce))

### Features

* add branding to admin site ([e06fcf8](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/e06fcf8))
* update python requirements ([0eaca19](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/0eaca19))
* **admin:** split admin into /admin and /backend to allow for proper user management ([891fca8](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/891fca8))

### Performance Improvements

* **charts:** disable window resize handler to prevent lockups ([0f3c636](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/0f3c636))



<a name="1.0.6"></a>
## [1.0.6](https://bitbucket.org/factoryconcepts/critical-path-mapping/compare/v1.0.5...v1.0.6) (2015-07-27)


### Bug Fixes

* **MAP:** Remove debugging data from MAP chart overlay ([a105904](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/a105904))
* **operations:** don't allow operations to stat before sheet release date ([892b901](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/892b901))
* **operations:** newly created operations don't throw error on immediate edit ([52ca282](https://bitbucket.org/factoryconcepts/critical-path-mapping/commits/52ca282))

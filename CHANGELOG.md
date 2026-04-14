# Changelog

All notable changes to this project will be documented in this file.

## Unreleased (2026-04-14)

### Builds

- **deps:** bump actions/github-script from 8 to 9 ([1d2b813](https://github.com/somaz94/commit-info-extractor/commit/1d2b813674757fc53fcfe502643dcd0ee0a1bf81))

<br/>

## [v1.4.2](https://github.com/somaz94/commit-info-extractor/compare/v1.4.1...v1.4.2) (2026-04-03)

### Code Refactoring

- extract dedup helper, narrow exception catches, and clean up redundant checks ([7c7cc63](https://github.com/somaz94/commit-info-extractor/commit/7c7cc633b1f80c62f25941dd02ed8b1be8cab0be))

### Documentation

- remove duplicate rules covered by global CLAUDE.md ([df4bd2a](https://github.com/somaz94/commit-info-extractor/commit/df4bd2a34fdff1522a4c2fe739b21b70fca2c3c7))

### Chores

- remove duplicate rules from CLAUDE.md (moved to global) ([95074d9](https://github.com/somaz94/commit-info-extractor/commit/95074d9f1993b11ce2ada756199c0bce79ae7d3c))
- add git config protection to CLAUDE.md ([602f73b](https://github.com/somaz94/commit-info-extractor/commit/602f73ba5b611dda8d1a689d79f9fa886fa76e94))

### Contributors

- somaz

<br/>

## [v1.4.1](https://github.com/somaz94/commit-info-extractor/compare/v1.4.0...v1.4.1) (2026-03-25)

### Bug Fixes

- improve security and error handling ([d9020b8](https://github.com/somaz94/commit-info-extractor/commit/d9020b80474f449eaf5a12e96d3190f3a0a80560))
- use heredoc to safely print outputs containing special characters ([526c9e7](https://github.com/somaz94/commit-info-extractor/commit/526c9e745a66ca28d0aefeff389c12b7dc33bbc1))
- use env vars for outputs to avoid shell injection from special characters ([f86cf55](https://github.com/somaz94/commit-info-extractor/commit/f86cf55d4a44ca216ecfd5330700f73041ec4269))
- apache license -> mit license ([58602b2](https://github.com/somaz94/commit-info-extractor/commit/58602b2f87d758f495001149d361198367fad527))
- delete linter.yml ([21b852a](https://github.com/somaz94/commit-info-extractor/commit/21b852a0aeb8a393cbff7341f5f7e19aba167a1b))

### Documentation

- add no-push rule to CLAUDE.md ([cfd6509](https://github.com/somaz94/commit-info-extractor/commit/cfd6509240ffbcc189d94e655401364cf806a3d5))
- update CLAUDE.md with commit guidelines and language ([1ff13ad](https://github.com/somaz94/commit-info-extractor/commit/1ff13ad323c48418916464a6f2e36ebb24dcc2df))

### Continuous Integration

- skip auto-generated changelog and contributors commits in release notes ([21fa432](https://github.com/somaz94/commit-info-extractor/commit/21fa432bd8e1ccac4a76be0d72d4c8d4a664ca98))
- revert to body_path RELEASE.md in release workflow ([c2a9972](https://github.com/somaz94/commit-info-extractor/commit/c2a997256655cfc394f8df4c69a5fcca4402e606))
- use generate_release_notes instead of RELEASE.md ([da012bd](https://github.com/somaz94/commit-info-extractor/commit/da012bd64a10bfa79639461f9cec201a7b047a1d))
- migrate gitlab-mirror workflow to multi-git-mirror action ([44f4741](https://github.com/somaz94/commit-info-extractor/commit/44f4741a89f4e5b102d9ec0b8a16ac2538a5352b))
- use somaz94/contributors-action@v1 for contributors generation ([8caae8b](https://github.com/somaz94/commit-info-extractor/commit/8caae8b2645974f2ef9e5e9889f4a67735a98857))
- use major-tag-action for version tag updates ([ded94a1](https://github.com/somaz94/commit-info-extractor/commit/ded94a1ed3d6935b76279c613057cfaa2dad7c20))
- add all missing workflow files and release config ([9ac3aad](https://github.com/somaz94/commit-info-extractor/commit/9ac3aad61c8e0b00dfd3d43d2eb71d2a42210011))

### Chores

- change license from MIT to Apache 2.0 ([de0389a](https://github.com/somaz94/commit-info-extractor/commit/de0389a553f40db863d9f9ca6e96f82b1608f69b))
- remove linter workflow and config files ([0396980](https://github.com/somaz94/commit-info-extractor/commit/03969806aa71fee03b55e7105063e4b53caf0f01))

### Contributors

- somaz

<br/>

## [v1.4.0](https://github.com/somaz94/commit-info-extractor/compare/v1.3.2...v1.4.0) (2026-03-10)

### Features

- add extract_pattern, commit_range inputs and match_count output ([f1a8018](https://github.com/somaz94/commit-info-extractor/commit/f1a8018108b7e7e90a990fbd2736fb60d072ea7d))
- add extract_pattern, commit_range inputs and match_count output ([bc9aa7c](https://github.com/somaz94/commit-info-extractor/commit/bc9aa7cb38fa2425f52b6e5b23b50a46d02e3523))
- add extract_pattern, commit_range inputs and match_count output ([93c398f](https://github.com/somaz94/commit-info-extractor/commit/93c398feac92262e2e78a4eae638208f69e38397))

### Code Refactoring

- modularize entrypoint.py into app/ package ([2d94593](https://github.com/somaz94/commit-info-extractor/commit/2d94593095f5000fa28c67f750b66f24b324411f))
- modularize entrypoint.py into app/ package ([7998756](https://github.com/somaz94/commit-info-extractor/commit/7998756083426ed6525754d073e4d68143344292))

### Documentation

- test/TESTING.md ([f0841de](https://github.com/somaz94/commit-info-extractor/commit/f0841de9a181234070a5014943eb7a3212cf529b))
- update TESTING.md and README.md for modular app structure ([5a34c56](https://github.com/somaz94/commit-info-extractor/commit/5a34c561c8afb6bd80ba8c2eea6396889f6ce5ec))
- README.md ([ba90e64](https://github.com/somaz94/commit-info-extractor/commit/ba90e643516c13f5d5bf5e1d33f3ac1662e6d7c3))
- README.md ([e48ab75](https://github.com/somaz94/commit-info-extractor/commit/e48ab7522e18ba1f53e950c44935d72128a02a3f))

### Builds

- **deps:** bump actions/setup-python from 5 to 6 ([6869294](https://github.com/somaz94/commit-info-extractor/commit/6869294c4114c85cca3c68a834a49ffbeb35fd4b))

### Contributors

- somaz

<br/>

## [v1.3.2](https://github.com/somaz94/commit-info-extractor/compare/v1.3.1...v1.3.2) (2025-11-27)

### Code Refactoring

- entrypoint.py ([6962392](https://github.com/somaz94/commit-info-extractor/commit/696239243ca764534026bfa74221306b764d8962))

### Contributors

- somaz

<br/>

## [v1.3.1](https://github.com/somaz94/commit-info-extractor/compare/v1.3.0...v1.3.1) (2025-11-27)

### Code Refactoring

- code ([dea6940](https://github.com/somaz94/commit-info-extractor/commit/dea694084ae031d4eb5dea84f03e9fa227c03ddc))

### Chores

- use-action.yml ([73a317b](https://github.com/somaz94/commit-info-extractor/commit/73a317bd99db96104d5aeb10cdabdbf278407ba7))

### Contributors

- somaz

<br/>

## [v1.3.0](https://github.com/somaz94/commit-info-extractor/compare/v1.2.1...v1.3.0) (2025-11-27)

### Code Refactoring

- bash -> python ([077366c](https://github.com/somaz94/commit-info-extractor/commit/077366cfac80119fbe80c059273639307f1b1d5e))

### Documentation

- README.md ([8bba1f7](https://github.com/somaz94/commit-info-extractor/commit/8bba1f71ca645c1110d96ca5823ab4ff7759d808))

### Builds

- **deps:** bump actions/checkout from 5 to 6 ([8ea350d](https://github.com/somaz94/commit-info-extractor/commit/8ea350df071b1d95995451e822ee0e25c942174b))
- **deps:** bump actions/checkout from 4 to 5 ([b6a4482](https://github.com/somaz94/commit-info-extractor/commit/b6a448255737ffc2531043d8d9ffb8b9c9e568aa))
- **deps:** bump super-linter/super-linter from 7 to 8 ([f6072f2](https://github.com/somaz94/commit-info-extractor/commit/f6072f2311523e4c20444f09302bcdeb08c436b3))
- **deps:** bump alpine from 3.21 to 3.22 in the docker-minor group ([bc6779d](https://github.com/somaz94/commit-info-extractor/commit/bc6779ddd88d17a227d7eba29504eed30f87d196))

### Chores

- use-action.yml ([6a33f4e](https://github.com/somaz94/commit-info-extractor/commit/6a33f4ebf899ef2181fb8c27b09a6b74980c42c4))
- ci.yml ([502a7dc](https://github.com/somaz94/commit-info-extractor/commit/502a7dcda787bb1dd74f897b73b89094ec314fa7))
- entrypoint.py ([718ef7e](https://github.com/somaz94/commit-info-extractor/commit/718ef7eebabb1612d66bee3bd4ae7cb48d3e8e13))
- entrypoint.py, test ([bab2701](https://github.com/somaz94/commit-info-extractor/commit/bab270131f2fe5863378d86ddf5c76067b29ea1e))
- stale-issues, issue-greeting ([0aaff17](https://github.com/somaz94/commit-info-extractor/commit/0aaff179615ad87e180ab0fe345ed6913e749fc7))
- dockerignore ([5eb2d67](https://github.com/somaz94/commit-info-extractor/commit/5eb2d67c765b9fe0a3e0e6275f57a341eadadfae))
- release.yml ([dcd559d](https://github.com/somaz94/commit-info-extractor/commit/dcd559d30dbdd660e356aeeac387d93dcb68baea))
- workflows ([f317966](https://github.com/somaz94/commit-info-extractor/commit/f3179669870912bc64ab5ce501740f9f78069952))

### Contributors

- somaz

<br/>

## [v1.2.1](https://github.com/somaz94/commit-info-extractor/compare/v1.2.0...v1.2.1) (2025-04-11)

### Documentation

- README.md ([1cc7a26](https://github.com/somaz94/commit-info-extractor/commit/1cc7a265736b873783409fbd9e08366f12ba20ca))
- README.md, fix: action.yml, entrypoint.sh ([f3b96af](https://github.com/somaz94/commit-info-extractor/commit/f3b96af3d7ec9ac47c844281127aa31b407ae52c))
- README.md ([2e071d6](https://github.com/somaz94/commit-info-extractor/commit/2e071d6da9fb00c608ac2b33848ca35295ef9138))

### Contributors

- somaz

<br/>

## [v1.2.0](https://github.com/somaz94/commit-info-extractor/compare/v1.1.0...v1.2.0) (2025-04-10)

### Bug Fixes

- use-action.yml, README.md, entrypoint.sh ([5901e38](https://github.com/somaz94/commit-info-extractor/commit/5901e380acc87eca4f21db02a43f4826a665b20a))
- entrypoint.sh ([fcbbe30](https://github.com/somaz94/commit-info-extractor/commit/fcbbe309abfc03f28a4e7092d92258c3f94db762))
- action.yml, entrypoint.sh, README.md, ci.yml ([47a6f2a](https://github.com/somaz94/commit-info-extractor/commit/47a6f2a8b215256b99330e556365e9c2660bdfa6))
- changelog-generator.yml ([ee8a438](https://github.com/somaz94/commit-info-extractor/commit/ee8a438fe92cf108789bd87a64a3b7eb1640194c))
- ci.yml ([39cb5ca](https://github.com/somaz94/commit-info-extractor/commit/39cb5caa35cc49ba1de12ab1836fa55122185020))
- changelog-generator.yml ([8db0c7a](https://github.com/somaz94/commit-info-extractor/commit/8db0c7a10405fbbccdf946095389669dec743daa))

### Add

- gitlab-mirror.yml ([2b55c66](https://github.com/somaz94/commit-info-extractor/commit/2b55c66b3252e7020d8190626108efb60356d5f2))

### Contributors

- somaz

<br/>

## [v1.1.0](https://github.com/somaz94/commit-info-extractor/compare/v1.0.5...v1.1.0) (2025-02-17)

### Bug Fixes

- action.yml, ci.yml, entrypoint.sh ([56383b4](https://github.com/somaz94/commit-info-extractor/commit/56383b48c53eb603058e82ea948ae715c8cb58f8))

### Documentation

- README.md ([2e1ed8f](https://github.com/somaz94/commit-info-extractor/commit/2e1ed8fb8dc922fae4477817787e877eae8a0e7a))

### Contributors

- somaz

<br/>

## [v1.0.5](https://github.com/somaz94/commit-info-extractor/compare/v1.0.4...v1.0.5) (2025-02-07)

### Features

- prettier ([19da493](https://github.com/somaz94/commit-info-extractor/commit/19da49326552ea15bedd6f70bedbfbb1825a2895))

### Bug Fixes

- ci.yml ([4e5f50a](https://github.com/somaz94/commit-info-extractor/commit/4e5f50adfab0737160737ae0050ff4c856ced89b))
- ci.yml ([73382be](https://github.com/somaz94/commit-info-extractor/commit/73382bec86121b941708266946ca2c37d7ccd056))
- entrypoint.sh , docs: README.md ([787d5f0](https://github.com/somaz94/commit-info-extractor/commit/787d5f053eee93db25b8688a85a90b51011f50aa))
- .github/workflows/* & entrypoint.sh , docs: README.md ([8b4e47b](https://github.com/somaz94/commit-info-extractor/commit/8b4e47b41e19987ce1cb561bf557643272924835))
- changelog-generator.yml ([2e0e140](https://github.com/somaz94/commit-info-extractor/commit/2e0e140131a8fa7a7f238bf2ce288dd9c0609db6))

### Documentation

- CODEOWNERS ([c63b0e1](https://github.com/somaz94/commit-info-extractor/commit/c63b0e119634928fcba87c952622d85e269f6467))
- README.md ([5af585b](https://github.com/somaz94/commit-info-extractor/commit/5af585b7c6fd61dee827e2070972db8191e5d2db))
- README.md ([184beab](https://github.com/somaz94/commit-info-extractor/commit/184beab2aca73f861323601d4a62349869c6ec9c))
- README.md ([080a3ce](https://github.com/somaz94/commit-info-extractor/commit/080a3cee2d8ad10c9d6efc80301133d54f3b6d72))
- README.md ([57d801d](https://github.com/somaz94/commit-info-extractor/commit/57d801ddb3bee1f3e4c3d0b8e7b658c1233b38bd))

### Builds

- **deps:** bump janheinrichmerker/action-github-changelog-generator ([7176ec9](https://github.com/somaz94/commit-info-extractor/commit/7176ec9019dccc6b839b909c146899a800f7d656))
- **deps:** bump alpine from 3.20 to 3.21 in the docker-minor group ([1db0e3e](https://github.com/somaz94/commit-info-extractor/commit/1db0e3e160067b882e91e25c80fa7d986868af4a))
- **deps:** bump super-linter/super-linter from 6 to 7 ([28ece8f](https://github.com/somaz94/commit-info-extractor/commit/28ece8ff8bc64ace0340586fa693e7b5a4fd9098))

### Chores

- fix changelog-generator.yml ([6da7f9e](https://github.com/somaz94/commit-info-extractor/commit/6da7f9e2692e0f33227806d65d1357cbea1fd1d7))
- fix changelog workflow ([c3bf4a2](https://github.com/somaz94/commit-info-extractor/commit/c3bf4a26f44f948b8a883f952b06f2beac952584))
- fix changelog workflow ([9e4b185](https://github.com/somaz94/commit-info-extractor/commit/9e4b18574ca07ad267ac262bfc17cb4634f91917))
- fix changelog workflow ([0b51348](https://github.com/somaz94/commit-info-extractor/commit/0b5134827e49279b015352724f29126b58f7f14e))
- fix Dockerfile ([4486bdb](https://github.com/somaz94/commit-info-extractor/commit/4486bdb1e298da9bb0cb09aa54ec071523bff661))
- fix workflow ([d2f3d47](https://github.com/somaz94/commit-info-extractor/commit/d2f3d472fc251d8b51a3fbe0414ae5d5fb57b9b7))
- delete linter workflow ([4921cb2](https://github.com/somaz94/commit-info-extractor/commit/4921cb254deb1b8de703c80b5030e631d4c6d2da))
- add changelog generator workflow ([b489188](https://github.com/somaz94/commit-info-extractor/commit/b48918884678b57b7a2def8cbef72a99ce998219))
- Dockerfile package version ([b0ff9e8](https://github.com/somaz94/commit-info-extractor/commit/b0ff9e88908067913fb044174f5ecabf4d930667))
- Dockerfile package version ([5fcc6ba](https://github.com/somaz94/commit-info-extractor/commit/5fcc6ba4f4f962ffc45adcffeba21628ccfcad34))

### Contributors

- somaz

<br/>

## [v1.0.4](https://github.com/somaz94/commit-info-extractor/compare/v1.0.3...v1.0.4) (2024-06-24)

### Bug Fixes

- entrypoint.sh ([52c87f1](https://github.com/somaz94/commit-info-extractor/commit/52c87f1ca015b2872160a8d014fc007a0928e346))
- entrypoint.sh ([5efc69b](https://github.com/somaz94/commit-info-extractor/commit/5efc69b9fc0295cea787adfc15dd6cfbafe6dd9b))
- entrypoint.sh ([d0aa196](https://github.com/somaz94/commit-info-extractor/commit/d0aa19692204b95654d4d58e3732f45ab0fc400d))
- action.yml ([a173c3e](https://github.com/somaz94/commit-info-extractor/commit/a173c3e3182be7dab0803d42607e4a700d4f9a62))

### Documentation

- README.md ([7c797b4](https://github.com/somaz94/commit-info-extractor/commit/7c797b422aea6212af7f4dfc04db870193277c9b))
- README.md ([cb50c92](https://github.com/somaz94/commit-info-extractor/commit/cb50c92538e5d2a9ed506bb1c13a88e511237d71))

### Contributors

- somaz

<br/>

## [v1.0.3](https://github.com/somaz94/commit-info-extractor/compare/v1.0.2...v1.0.3) (2024-06-20)

### Bug Fixes

- action.yml ([d0f6162](https://github.com/somaz94/commit-info-extractor/commit/d0f6162f86c06d2e0b1a059ba596b6288b4f8cda))
- .env.test ([e790c9d](https://github.com/somaz94/commit-info-extractor/commit/e790c9da0a398a7aa4bc9e48df1b44b1041c4f5a))
- use-action.yml ([2d6cf45](https://github.com/somaz94/commit-info-extractor/commit/2d6cf45b99e324b36a2dccfabc698c3d65f720b4))

### Contributors

- somaz

<br/>

## [v1.0.2](https://github.com/somaz94/commit-info-extractor/compare/v1.0.1...v1.0.2) (2024-06-20)

### Bug Fixes

- entrypoint.sh ([a7affcc](https://github.com/somaz94/commit-info-extractor/commit/a7affcc30e85189011ad17f51e02bbde4b4fe1a6))
- entrypoint.sh ([a178206](https://github.com/somaz94/commit-info-extractor/commit/a1782066472fe3c0d8d44c327161d2811d2fa566))
- use-action.yml ([c6c7e52](https://github.com/somaz94/commit-info-extractor/commit/c6c7e52cba92715eb8c13d38dc0c58695d1cb43a))

### Documentation

- README.md ([890c4ae](https://github.com/somaz94/commit-info-extractor/commit/890c4ae08c9acd7a4222bcc501881688f5fb835f))
- README.md ([034e3d5](https://github.com/somaz94/commit-info-extractor/commit/034e3d521a3aff1a282b5dc9ff903ef0f40f62d5))

### Contributors

- somaz

<br/>

## [v1.0.1](https://github.com/somaz94/commit-info-extractor/compare/v1.0.0...v1.0.1) (2024-06-19)

### Bug Fixes

- checkov.yml ([2bcaef1](https://github.com/somaz94/commit-info-extractor/commit/2bcaef1d8f12d576109aa5f4981e081f3cf695ec))
- test-action.yml ([e10513e](https://github.com/somaz94/commit-info-extractor/commit/e10513e473133d14eec89a0cec12372f47908487))
- test-action.yml ([fd85164](https://github.com/somaz94/commit-info-extractor/commit/fd851647505a52c2204a0dd8883647a340b7cc9f))

### Documentation

- README.md ([21133f9](https://github.com/somaz94/commit-info-extractor/commit/21133f96c0744b088f7215f1c39d723de5e92543))

### Delete

- tag.yml ([5db22c8](https://github.com/somaz94/commit-info-extractor/commit/5db22c894e45e0dacd9aea76fa7c290f849361b1))

### Contributors

- somaz

<br/>

## [v1.0.0](https://github.com/somaz94/commit-info-extractor/releases/tag/v1.0.0) (2024-06-19)

### Bug Fixes

- entrypoint.sh ([a470ee3](https://github.com/somaz94/commit-info-extractor/commit/a470ee3b9324fd5b102736d23627e38107471c9c))
- entrypoint.sh ([b452bc6](https://github.com/somaz94/commit-info-extractor/commit/b452bc6c79cbc788fcaf8adf13ff8d31f97e066f))
- action.yml & entrypoint.sh ([d5b6dc2](https://github.com/somaz94/commit-info-extractor/commit/d5b6dc244143bdbce4dde622366ffaa8e1b2ed85))
- entrypoint.sh & ci.yml ([179a653](https://github.com/somaz94/commit-info-extractor/commit/179a653e038e8fcffe90c165292d55dd255355f5))
- ci.yml ([53c1af7](https://github.com/somaz94/commit-info-extractor/commit/53c1af7a7a06e1d1c84dae14995aba8352e3937d))
- entrypoint.sh * ci.yml ([62d2a34](https://github.com/somaz94/commit-info-extractor/commit/62d2a34240727aa1e8dbf8370d440a11b02b2f19))
- entrypoint.sh ([5751e96](https://github.com/somaz94/commit-info-extractor/commit/5751e965d2530026818fe1b1cdb45e17d4fa2d9f))
- entrypoint.sh ([512ca89](https://github.com/somaz94/commit-info-extractor/commit/512ca89a90a336d969b6607458a06313a4054d43))
- entrypoint.sh & ci.yml ([9dc1b35](https://github.com/somaz94/commit-info-extractor/commit/9dc1b355bb4e079e29799410d0cd0461eebe4f3a))
- entrypoint.sh & ci.yml ([43f03bf](https://github.com/somaz94/commit-info-extractor/commit/43f03bf781d4690ab109b2572a2ffef4e15b100d))
- entrypoint.sh & ci.yml ([fa3e658](https://github.com/somaz94/commit-info-extractor/commit/fa3e658d04f619c756bb793dea65a36e28c5edae))
- entrypoint.sh & ci.yml ([09bae16](https://github.com/somaz94/commit-info-extractor/commit/09bae163ffc2dd3570e934c8e2ac8292db1d9113))
- entrypoint.sh ([0052205](https://github.com/somaz94/commit-info-extractor/commit/0052205739df8d429113fbb0ed821131eaff637d))
- ci.yml & entrypoint.sh ([cdce5b8](https://github.com/somaz94/commit-info-extractor/commit/cdce5b86f27d656944fa6366986232cb310936a9))
- Dockerfile & ci.yml ([0b888d7](https://github.com/somaz94/commit-info-extractor/commit/0b888d7332bd0c9af868f9c1754c51603d2f66e5))
- Dockerfile & ci.yml ([77936fc](https://github.com/somaz94/commit-info-extractor/commit/77936fcfcce82f0fffb56687843c0266f2a59fd5))
- Dockerfile & ci.yml ([850ac96](https://github.com/somaz94/commit-info-extractor/commit/850ac969e44c71b0fd0ec146d748f293beffc216))
- Dockerfile & ci.yml ([ff2ac20](https://github.com/somaz94/commit-info-extractor/commit/ff2ac20203c823863b3ae2307415fde01ec0a2ed))
- Dockerfile & ci.yml ([39cf1f6](https://github.com/somaz94/commit-info-extractor/commit/39cf1f61e731df2accc0dcedc46827a4ddbcffb3))
- ci.yml ([38e70c8](https://github.com/somaz94/commit-info-extractor/commit/38e70c81b5c8e6db0c41f02c5dc1d0e5c79100dc))
- Dockerfile & ci.yml ([c321b50](https://github.com/somaz94/commit-info-extractor/commit/c321b50fae2617875113c91e66bc970c74345842))
- ci.yml ([0570b6e](https://github.com/somaz94/commit-info-extractor/commit/0570b6ea729f270843e73092920ec5365a4122dc))
- ci.yml ([b9cb82a](https://github.com/somaz94/commit-info-extractor/commit/b9cb82ab31db9767eb9ca86cac5be03efd9ee2ab))
- action.yml & entrypoint.sh ([2054e95](https://github.com/somaz94/commit-info-extractor/commit/2054e955bf145c9dd2f95291076f9cd18bcec6eb))
- ci.yml & entrypoint.sh ([d03c3fc](https://github.com/somaz94/commit-info-extractor/commit/d03c3fcbda68c62d452cc74e83941c095a6eead6))
- entrypoint.sh ([1c983c2](https://github.com/somaz94/commit-info-extractor/commit/1c983c274ffa217dec2930cbafee66c8323fe537))

### Documentation

- README.md ([eac4a78](https://github.com/somaz94/commit-info-extractor/commit/eac4a78ad24131a31a286e22b5300623c869bdd1))
- README.md ([d5ed988](https://github.com/somaz94/commit-info-extractor/commit/d5ed988c1d69228a46f94d8b403e5cdfbda36d19))
- README.md ([a48caf6](https://github.com/somaz94/commit-info-extractor/commit/a48caf6f3a9250f198f034e079cd445029c3612b))
- README.md ([6028504](https://github.com/somaz94/commit-info-extractor/commit/6028504aca46d86e64b2e9c1cbbcf6d72d673a53))
- README.md ([00f9b05](https://github.com/somaz94/commit-info-extractor/commit/00f9b050d09ca4a33d7c42d81ffba36db64ba965))
- README.md ([479a630](https://github.com/somaz94/commit-info-extractor/commit/479a63049d67259a2f24142a5da0a07e2cb6789a))
- README.md ([bd291d1](https://github.com/somaz94/commit-info-extractor/commit/bd291d1569423f4d80fc286164c77839f1aeafd7))
- README.md ([d21e117](https://github.com/somaz94/commit-info-extractor/commit/d21e117063227d7d9eb72eeb736a77b0a3979a55))
- README.md ([e720491](https://github.com/somaz94/commit-info-extractor/commit/e720491ce083bfa9e120debca4619867b0b2663c))
- README.md ([37f0cae](https://github.com/somaz94/commit-info-extractor/commit/37f0cae2d58b19afe4a699db045f9f11de8bd0de))
- README.md ([bef2425](https://github.com/somaz94/commit-info-extractor/commit/bef24255a732034f6d157b948157849f8553a817))
- README.md ([cf4712e](https://github.com/somaz94/commit-info-extractor/commit/cf4712e1617da5572dbb80aa887bd7655f0f1c16))

### Tests

- commit-info-extractor action template ([2492a87](https://github.com/somaz94/commit-info-extractor/commit/2492a87bf281b4dee16abf7fb3d8e10e1f78885e))
- commit-info-extractor action template ([f69ab06](https://github.com/somaz94/commit-info-extractor/commit/f69ab06ac84b720725be9fb04df905398c81c25c))
- commit-info-extractor action template ([78c74f6](https://github.com/somaz94/commit-info-extractor/commit/78c74f61d9817f89dd068ffdbea95a2ed5661178))
- commit-info-extractor action template ([ca74478](https://github.com/somaz94/commit-info-extractor/commit/ca74478e325d36b06c9b3907ea08e0685f656c42))

### Builds

- **deps:** bump docker/build-push-action from 5 to 6 ([b7b0b1d](https://github.com/somaz94/commit-info-extractor/commit/b7b0b1d3d9dd7af9bde8aebfee23569ba9db9df0))

### Contributors

- somaz

<br/>


# 地方競馬予測投票スケジューラー _(local-horse-racing-scheduler)_

[![.github/workflows/build.yml](https://github.com/u6k/investment-local-horse-racing-scheduler/actions/workflows/build.yml/badge.svg)](https://github.com/u6k/investment-local-horse-racing-scheduler/actions/workflows/build.yml) [![license](https://img.shields.io/github/license/u6k/local-horse-racing-scheduler.svg)](https://github.com/u6k/local-horse-racing-scheduler/blob/master/LICENSE) [![GitHub release](https://img.shields.io/github/release/u6k/local-horse-racing-scheduler.svg)](https://github.com/u6k/local-horse-racing-scheduler/releases) [![WebSite](https://img.shields.io/website-up-down-green-red/https/shields.io.svg?label=u6k.Redmine)](https://redmine.u6k.me/projects/local-horse-racing-scheduler) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

地方競馬自動投票システムをスケジュール制御する

本システムは、データ収集、予測、投票というモジュールが稼働している。各モジュールの実行タイミングを本モジュールで制御する。

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Others](#others)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Install

Dockerを使用します。

```
> docker version
Client:
 Version:           28.3.3-rd
 API version:       1.47 (downgraded from 1.51)
 Go version:        go1.24.5
 Git commit:        309deef
 Built:             Wed Jul 30 05:30:49 2025
 OS/Arch:           windows/amd64
 Context:           default

Server:
 Engine:
  Version:          27.3.1
  API version:      1.47 (minimum version 1.24)
  Go version:       go1.23.9
  Git commit:       41ca978a0a5400cc24b274137efa9f25517fcc0b
  Built:            Thu May  8 20:02:17 2025
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v2.0.0
  GitCommit:        207ad711eabd375a01713109a8a197d197ff6542
 runc:
  Version:          1.2.2
  GitCommit:        7cb363254b69e10320360b63fb73e0ffb5da7bf2
 docker-init:
  Version:          0.19.0
  GitCommit:
```

`docker pull`でイメージを取得します。

```
$ docker pull ghcr.io/u6k/local-horse-racing-scheduler:0.1.0-dev
```

## Usage

`docker run`でコンテナを実行します。

```
$ docker run --rm --env-file=.env ghcr.io/u6k/local-horse-racing-scheduler:0.1.0-dev
```

環境変数で動作を制御します。詳細は`.env.original`を参照してください。

## Others

最新の情報は、[Wiki | local-horse-racing-scheduler | u6k.Redmine](https://redmine.u6k.me/projects/local-horse-racing-scheduler/wiki)を参照してください。

## Maintainers

- u6k
    - [X](https://x.com/u6k_yu1)
    - [GitHub](https://github.com/u6k)
    - [Blog](https://blog.u6k.me/)

## Contributing

当プロジェクトに興味を持っていただき、ありがとうございます。[既存のチケット](https://redmine.u6k.me/projects/local-horse-racing-scheduler/issues)をご覧ください。

当プロジェクトは、[Contributor Covenant](https://www.contributor-covenant.org/version/3/0/code_of_conduct/)に準拠します。

## License

[MIT License](https://github.com/u6k/local-horse-racing-scheduler/blob/main/LICENSE)

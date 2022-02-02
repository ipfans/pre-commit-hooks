# pre-commit-hooks

`pre-commit-hooks` is self-managed repo for [pre-commit](https://pre-commit.com).

## Requirement

* Python 3
* pre-commit

### Dependencies (Optional with hooks)

```
go install mvdan.cc/gofumpt@latest  # required by `go-fumpt`
go install golang.org/x/tools/cmd/goimports@latest  # required by `go-imports`
go install github.com/fzipp/gocyclo/cmd/gocyclo@latest  # required by `go-cyclo`
go install github.com/go-critic/go-critic/cmd/gocritic@latest  # required by `go-critic`
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest  # required by `golangci-lint`
```

## Usage

### Setup

Write `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/ipfans/pre-commit-hooks
    rev: v0.1.3
    hooks:
      - id: go-fumpt
      - id: go-imports
      - id: go-vet
      - id: go-cyclo
        args: [-over=15]
      - id: golangci-lint
      - id: go-critic
      - id: go-unit-tests
      - id: go-build
      - id: go-generate
      - id: go-mod-tidy
      - id: commig-msg-checker
```

### installation

```
pre-commit install
pre-commit install --hook-type commit-msg  # Optional
```

@echo off
set "ROOT=technical-docs"

:: Create root directory
mkdir "%ROOT%"

:: Top-level files
type nul > "%ROOT%\README.md"
type nul > "%ROOT%\CHANGELOG.md"
type nul > "%ROOT%\CONTRIBUTING.md"

:: setup/
mkdir "%ROOT%\setup"
type nul > "%ROOT%\setup\prerequisites.md"
type nul > "%ROOT%\setup\local-setup.md"
type nul > "%ROOT%\setup\docker.md"
type nul > "%ROOT%\setup\config.md"

:: development/
mkdir "%ROOT%\development"
type nul > "%ROOT%\development\code-structure.md"
type nul > "%ROOT%\development\style-guide.md"
type nul > "%ROOT%\development\framework-overview.md"
type nul > "%ROOT%\development\tooling.md"
type nul > "%ROOT%\development\debugging.md"

:: build-deploy/
mkdir "%ROOT%\build-deploy"
type nul > "%ROOT%\build-deploy\build.md"
type nul > "%ROOT%\build-deploy\ci-cd.md"
type nul > "%ROOT%\build-deploy\deployment.md"
type nul > "%ROOT%\build-deploy\rollback.md"

:: usage/
mkdir "%ROOT%\usage"
type nul > "%ROOT%\usage\cli.md"
type nul > "%ROOT%\usage\api-usage.md"
type nul > "%ROOT%\usage\integration-examples.md"
type nul > "%ROOT%\usage\faq.md"

:: testing/
mkdir "%ROOT%\testing"
type nul > "%ROOT%\testing\overview.md"
type nul > "%ROOT%\testing\unit.md"
type nul > "%ROOT%\testing\integration.md"
type nul > "%ROOT%\testing\e2e.md"
type nul > "%ROOT%\testing\mocking.md"

:: monitoring/
mkdir "%ROOT%\monitoring"
type nul > "%ROOT%\monitoring\logging.md"
type nul > "%ROOT%\monitoring\metrics.md"
type nul > "%ROOT%\monitoring\alerts.md"
type nul > "%ROOT%\monitoring\troubleshooting.md"

:: scripts/
mkdir "%ROOT%\scripts"
type nul > "%ROOT%\scripts\build.sh"
type nul > "%ROOT%\scripts\deploy.sh"
type nul > "%ROOT%\scripts\lint.sh"
type nul > "%ROOT%\scripts\test.sh"

:: references/
mkdir "%ROOT%\references"
type nul > "%ROOT%\references\links.md"
type nul > "%ROOT%\references\dependencies.md"
type nul > "%ROOT%\references\glossary.md"

echo Project directory structure created under %ROOT%
pause

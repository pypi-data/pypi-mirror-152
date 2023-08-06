# Changelog

## [v5.0.0](https://github.com/GENESIS-EFRC/reaction-network/tree/v5.0.0) (2022-03-31)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v4.3.0...v5.0.0)

**Fixed bugs:**

- `ChemicalPotentialDiagram.metastable_domains` occasionally does not work for some systems, particularly with large \# elements [\#91](https://github.com/GENESIS-EFRC/reaction-network/issues/91)

**Closed issues:**

- Setup Issue \(setuptools-scm was unable to detect version for\) [\#105](https://github.com/GENESIS-EFRC/reaction-network/issues/105)

**Merged pull requests:**

- Add support for multiprocessing via ray, add builders and pydantic models, bug fixes [\#106](https://github.com/GENESIS-EFRC/reaction-network/pull/106) ([mattmcdermott](https://github.com/mattmcdermott))
- Fix broken metastable\_domains in chemical potential diagram [\#102](https://github.com/GENESIS-EFRC/reaction-network/pull/102) ([mattmcdermott](https://github.com/mattmcdermott))

## [v4.3.0](https://github.com/GENESIS-EFRC/reaction-network/tree/v4.3.0) (2022-03-02)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v4.2.0...v4.3.0)

**Fixed bugs:**

- `NISTReferenceEntry` is sometimes incorrect for phases with multiple entries having different formulas [\#89](https://github.com/GENESIS-EFRC/reaction-network/issues/89)
- Minimize enumerators slow when exclusive precursors specified [\#87](https://github.com/GENESIS-EFRC/reaction-network/issues/87)
- `get_computed_rxn` behaving very slow [\#86](https://github.com/GENESIS-EFRC/reaction-network/issues/86)

**Merged pull requests:**

- Update Github action for release [\#100](https://github.com/GENESIS-EFRC/reaction-network/pull/100) ([mattmcdermott](https://github.com/mattmcdermott))
- Fix for broken NIST data and small speedups for e\_above\_hull calculations [\#90](https://github.com/GENESIS-EFRC/reaction-network/pull/90) ([mattmcdermott](https://github.com/mattmcdermott))

## [v4.2.0](https://github.com/GENESIS-EFRC/reaction-network/tree/v4.2.0) (2022-02-11)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v4.1.0...v4.2.0)

**Closed issues:**

- Unnecessary computations in Enumerators with `exclusive_precursors=True` [\#77](https://github.com/GENESIS-EFRC/reaction-network/issues/77)

**Merged pull requests:**

- Address several performance issues, add FREED data, support for metastable CPDs [\#88](https://github.com/GENESIS-EFRC/reaction-network/pull/88) ([mattmcdermott](https://github.com/mattmcdermott))

## [v4.1.0](https://github.com/GENESIS-EFRC/reaction-network/tree/v4.1.0) (2022-02-01)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v4.0.2...v4.1.0)

**Closed issues:**

- Unnecessary calculations occurring when exclusive\_precursors=True [\#76](https://github.com/GENESIS-EFRC/reaction-network/issues/76)

**Merged pull requests:**

- Speed up enumerators and tests [\#85](https://github.com/GENESIS-EFRC/reaction-network/pull/85) ([mattmcdermott](https://github.com/mattmcdermott))

## [v4.0.2](https://github.com/GENESIS-EFRC/reaction-network/tree/v4.0.2) (2022-01-22)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v4.0.1...v4.0.2)

## [v4.0.1](https://github.com/GENESIS-EFRC/reaction-network/tree/v4.0.1) (2022-01-22)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v4.0.0...v4.0.1)

**Merged pull requests:**

- Fix github workflows [\#75](https://github.com/GENESIS-EFRC/reaction-network/pull/75) ([mattmcdermott](https://github.com/mattmcdermott))

## [v4.0.0](https://github.com/GENESIS-EFRC/reaction-network/tree/v4.0.0) (2022-01-22)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v3.0.0...v4.0.0)

**Merged pull requests:**

- New NetworkFW, competitiveness scores, updates to enumerators, and bug fixes + speed-ups [\#59](https://github.com/GENESIS-EFRC/reaction-network/pull/59) ([mattmcdermott](https://github.com/mattmcdermott))

## [v3.0.0](https://github.com/GENESIS-EFRC/reaction-network/tree/v3.0.0) (2021-10-01)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v2.0.3...v3.0.0)

**Merged pull requests:**

- \[WIP\] Add much-needed tests [\#45](https://github.com/GENESIS-EFRC/reaction-network/pull/45) ([mattmcdermott](https://github.com/mattmcdermott))

## [v2.0.3](https://github.com/GENESIS-EFRC/reaction-network/tree/v2.0.3) (2021-08-05)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v2.0.2...v2.0.3)

**Merged pull requests:**

- Update README and trigger release [\#34](https://github.com/GENESIS-EFRC/reaction-network/pull/34) ([shyamd](https://github.com/shyamd))

## [v2.0.2](https://github.com/GENESIS-EFRC/reaction-network/tree/v2.0.2) (2021-08-05)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v2.0.1...v2.0.2)

**Merged pull requests:**

- Bug fix for interdependent reactions [\#33](https://github.com/GENESIS-EFRC/reaction-network/pull/33) ([mattmcdermott](https://github.com/mattmcdermott))

## [v2.0.1](https://github.com/GENESIS-EFRC/reaction-network/tree/v2.0.1) (2021-08-05)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v2.0.0...v2.0.1)

**Merged pull requests:**

- Fix and deploy docs [\#32](https://github.com/GENESIS-EFRC/reaction-network/pull/32) ([shyamd](https://github.com/shyamd))

## [v2.0.0](https://github.com/GENESIS-EFRC/reaction-network/tree/v2.0.0) (2021-08-05)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/paper...v2.0.0)

**Merged pull requests:**

- Major refactor of entire reaction-network package [\#23](https://github.com/GENESIS-EFRC/reaction-network/pull/23) ([mattmcdermott](https://github.com/mattmcdermott))

## [paper](https://github.com/GENESIS-EFRC/reaction-network/tree/paper) (2021-04-15)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/v1.0...paper)

**Merged pull requests:**

- Merging of major revision reaction-network code [\#5](https://github.com/GENESIS-EFRC/reaction-network/pull/5) ([mattmcdermott](https://github.com/mattmcdermott))
- Repo Cleanup [\#4](https://github.com/GENESIS-EFRC/reaction-network/pull/4) ([shyamd](https://github.com/shyamd))

## [v1.0](https://github.com/GENESIS-EFRC/reaction-network/tree/v1.0) (2020-07-21)

[Full Changelog](https://github.com/GENESIS-EFRC/reaction-network/compare/e55a689a4076416b181324eabb8066566c3c3a8e...v1.0)

**Merged pull requests:**

- Added pathway balancing, NIST gas data, StructuralComplexity cost metric, and more. [\#3](https://github.com/GENESIS-EFRC/reaction-network/pull/3) ([mattmcdermott](https://github.com/mattmcdermott))
- Implemented Gibbs Free Energy SISSO descriptor  [\#2](https://github.com/GENESIS-EFRC/reaction-network/pull/2) ([mattmcdermott](https://github.com/mattmcdermott))
- Added refactoring and documentation [\#1](https://github.com/GENESIS-EFRC/reaction-network/pull/1) ([mattmcdermott](https://github.com/mattmcdermott))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*

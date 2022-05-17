<div align="center">
    <h1>Awesome Systematic (Futures) Trading</h1>
</div>

We're collecting (an admittedly opinionated) list of resources papers, datasets, blogs, libraries, books and methodologies for finding, developing, and running Systematic Trading (Quantitative Trading) on Futures.

How do we pick the resources?

- Fit in systematic futures trading domain
- Focus on mid/low frequency strategies for tradability
- Rational giving reasonable probability to bring above market performances

*We're only at the beginning, and you can help by contributing to this GitHub!*

<!-- omit in toc -->
## How Can I Help?

If you're interested in this area and would like to hear more, join our [mailing list](#)! We'd also appreciate if you could fill out this short [form](#) to help us better understand what your interests might be.

<!-- omit in toc -->
### Feedback

If you have ideas on how we can make this repository better, feel free to submit an issue with suggestions.

<!-- omit in toc -->
### Contributing

We want this resource to grow with contributions from readers and data enthusiasts. If you'd like to make contributions to this Github repository, please read our contributing guidelines.

<!-- omit in toc -->
# Table of Content

- [Strategy Papers](#strategy-papers)
- [Datasets (coming soon)](#datasets-coming-soon)
- [Modeling Methodology (coming soon)](#modeling-methodology-coming-soon)
- [Books](#books)
- [Blogs](#blogs)
- [Basic Libraries](#basic-libraries)

# Strategy Papers

[Strategy Papers Area Page](strategy-papers.md)

List of **89 scientific papers** describing original systematic futures trading strategies. Each strategy is categorized by its asset class (Bonds, Commodities, Cryptos, Currencies, Equities), ordered by descending Sharpe ratio, and described by its Sharpe ratio, volatility and period of rebalancing.

<!-- omit in toc -->
### Example

[Market Closure and Short-Term Reversal](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2730304)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.89         | 7.69%      | Weekly                |


# Datasets (coming soon)

[Datasets Area Page](datasets.md)

List of **82 futures datasets** covering prices, volumes, COT, and much more.

<!-- omit in toc -->
### Example

| Ticker | Name                    | Exchange | Link          |
|--------|-------------------------|----------|---------------|
| BO     | Soybean Oil             | CME      | [Download](#) |


# Modeling Methodology (coming soon)

[Modeling Methodology Area Page](modeling-methodology.md)

This section outlines a methodology for identifying systematic training signals.


# Books

[Books Area Page](books.md)

A comprehensive list of books for quantitative traders.


# Blogs

- [Proof Engineering: The Algorithmic Trading Platform](https://medium.com/prooftrading/proof-engineering-the-algorithmic-trading-platform-b9c2f195433d)
- [Max Dama on Automated Trading](http://isomorphisms.sdf.org/maxdama.pdf)


# Basic Libraries

Machine learning:

- [MlFinLab (Hudson & Thames)](https://github.com/edarchimbaud/mlfinlab) - MlFinLab helps portfolio managers and traders who want to leverage the power of machine learning by providing reproducible, interpretable, and easy to use tools.
- [QLib (Microsoft)](https://github.com/microsoft/qlib) - Qlib is an AI-oriented quantitative investment platform, which aims to realize the potential, empower the research, and create the value of AI technologies in quantitative investment. With Qlib, you can easily try your ideas to create better Quant investment strategies. An increasing number of SOTA Quant research works/papers are released in Qlib.


Metrics computation:

- [quantstats](https://github.com/ranaroussi/quantstats) - Portfolio analytics for quants, written in Python

Visualization:

- [D-Tale (Man Group)](https://github.com/man-group/dtale) - D-Tale is the combination of a Flask back-end and a React front-end to bring you an easy way to view & analyze Pandas data structures.
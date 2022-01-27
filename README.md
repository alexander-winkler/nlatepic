[![DOI](https://zenodo.org/badge/324364381.svg)](https://zenodo.org/badge/latestdoi/324364381)

# Database of Neo-Latin Epic Poems

There has been considerable progress in the field of Neo-Latin epic poetry in recent years. This very basic database aims at bringing together the titles that have been mentioned in various overviews on the topic (Braun 2007, Braun 2020, Hofmann 2001, @gwynneEpic2017).

I have also created a public [zotero group on Neo-Latin epic poetry](https://www.zotero.org/groups/2680665/neolatin_epic). Feel free to contribute!

The very defition of 'epic poetry' is far from clear and undisputed. Most epic poems are longish narrative texts in hexameters. However, shorter narrative poems can also qualify as 'epic' poems (they can also be referred to as 'epyllia', an equally problematic term, cf. korenjakShortMythologicalEpic2012). There are even narrative texts in the elegiac metre that some might consider 'epic', e.g. Bargaeus' 'De Radagasi caede elegia' (differently @moulNeoLatinPoetry15002016).

Ludwig Braun's (2007: 1) definition:

> Unter einem Epos verstehe ich eine
> erzählende Dichtung in lateinischen Hexametern, die einen Umfang
> von mehr als einem Buch hat oder doch nach der ursprünglichen
> Absicht des Verfassers offenbar einmal haben sollte.



Currently, the data is stored and maintained in a simple `json` file (`works.json`). I am still working on a viable JSON Schema to describe the data with a sufficient degree of complexity. I try to add authority file ids to the authors and bibliographic ids to the prints in order to make them more easily retrievable.

The bibliographic references use the Zotero citation keys from the collection mentioned above.

If you want to contribute, [create an issue on github](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/creating-an-issue) or send me an email ({first name}\_{name}{at}posteo{dot}de).


 


# Todo

## Technical

* Revise Schema:
  + allow for more than one author
  + add contributor/publisher/translator
  + convert author > ID type from array to object with list of properties (wikidata, DNB, BNF, VIAF)

## Research

* Look through IJsewijn/Sacré 1998 and other overviews and add data.
* Look through Jensen, Minna Skafte. 1995. A History of Nordic Neo-Latin Literature. University Press of Southern Denmark.
* Develop decent frontend (maybe similar to [Catalogue of Critical Editions](https://dig-ed-cat.acdh.oeaw.ac.at/browsing/editions/), open source on [github](https://github.com/acdh-oeaw/dig_ed_cat)). Maybe the [json-editor](https://github.com/json-editor/json-editor) can be adapted.
* Enrich (meta-)data both manually and semi-automatically.


# Licence

The database is deeply indebted to the mentioned sources. The data collected here is provided under a CC0 licence, so feel free to use and develop it as you like.

<a title="Creative Commons, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:CC0_button.svg"><img width="64" alt="CC0 button" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/CC0_button.svg/64px-CC0_button.svg.png"></a>

If you want to refer to this database, you can cite it as follows:

*Winkler, Alexander: "Database of Neo-Latin Epic Poems", 2021-, http://doi.org/10.5281/zenodo.4393854*

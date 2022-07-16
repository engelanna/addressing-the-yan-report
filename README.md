---
marp: true
---

# Trial 1: [The Yan report](https://zenodo.org/record/4028830#.X1_bxGhKg2y)

In September 2020, the above claimed to **be** scientific evidence for SARS-CoV-2 being an engineered bioweapon :fearful: Zenodo granting it a Digital Object Identifier (DOI) made the report appear credible, despite the lack of peer review.

<br>The Johns Hopkins University countered with a [page-by-page account](https://www.centerforhealthsecurity.org/our-work/pubs_archive/pubs-pdfs/2020/200921-in-response-yan.pdf) of why they found the report unconvincing. However, neither their authority, nor having to read a mountain of references, would appeal to the conspiratorial :raised_eyebrow: part of the audience.

<br>Critical thinking only requires that __the core claim__ be verified - should _that_ turn out to be false, anything derived from it automatically becomes false as well :woman_shrugging: What was the postulate, then, that sufficed for its authors to be able to seek asylum in the USA?

---

## Restriction enzymes around the spike protein receptor binding motif

Mikolaj Raszek, PhD, was kind enough to elucidate, in [SARS-CoV-2 coronavirus origins alternative theories – do they hold up against science?](https://merogenomics.ca/blog/en/117/SARS-CoV-2_coronavirus_origins_alternative_theories__do_they_hold_up_against_science_Part_2), the core claim of the Yan report.

Two restriction enzymes (sequences bacteria use to slash virii to bits, repurposed by humans to glue parts of different genomes together): [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) and [BstEII](https://www.neb.com/products/r0162-bsteii#Product%20Information). According to Yan et al, the sequence between them allowed for targetting mammals larger than bats.
![Heart of the Yan report](https://user-images.githubusercontent.com/13955209/179063218-748bafb5-5ad1-4f32-a4da-89bd1e3e259f.png)

---

## Download the earliest known SARS-CoV-2 genome :arrow_down: (1 of 2)

<br>Yan et al's image caption cites the isolate **Wuhan-Hu-1** (isolate: a population of organisms having little genetic mixing with other organisms of the same species).

<br>![Aaa](https://user-images.githubusercontent.com/13955209/179288273-5f752b8d-1ed1-4a64-bf0d-61e9d792fe59.png)

<br>Viewing [the isolate at _NCBI Virus_](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=Severe%20acute%20respiratory%20syndrome%20coronavirus%202,%20taxid:2697049&IsolateParsed_s=Wuhan-Hu-1), the absolutely earliest accession (unique sequence identifier) is [MN908947.1](https://www.ncbi.nlm.nih.gov/nuccore/MN908947.1), collected in Dec 2019 :arrow_right: submitted 2020-01-05 :arrow_right: released 2020-01-12.

<br>That's 2 months until the World Health Organization would declare COVID-19 a pandemic ☣️ (2020-03-11).

---

## Download the earliest known SARS-CoV-2 genome :arrow_down: (2 of 2)

Switching to the FASTA format (a text format often used to store full genomes) allows us to download the troublemaker's genome:

![Downloading](https://user-images.githubusercontent.com/13955209/179091431-050a1882-24e8-4591-b176-d2d905f269aa.png)

As far as genomes go, this one's really tiny: a hundred thousand times shorter than a human one. A single human cell's genome would consume __at the very least__ 3.3 GB of your hard drive, you having ~37 trillion of those :see_no_evil: (luckily, only one is usually needed).

---

## Are EcoRI and BstEII _actually there_? :mag::eyes: (1 of 3)

<br>You can open the downloaded SARS-CoV-2 genome in a text editor :clipboard:, and search (`Ctrl+f` / `Cmd+f`) for the occurrences of the [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) sequence __GAATTC__ yourself. If you fancy a dopamine rush, __stop reading and go ahead now__ :grinning:

<br>The __N__ (= whichever letter) in [BstEII](https://www.neb.com/products/r0162-bsteii#Product%20Information)'s __GTTNACC__ is a tad more problematic, though. If you can locate _regular expression mode_ (look for a button marked `.*`) :crossed_fingers:, this hurdle can be cleared by inputting __GGT[ACGT]ACC__.

---

## Are EcoRI and BstEII _actually there_? :mag::eyes: (2 of 3)

<br>[Bioinformatics algorithms: An active learning approach](https://bioinformaticsalgorithms.com/faqs/replication.html) (search for `approximation`) provides a formula for computing the __approximate__ probability of a k-mer (word of size k) occurring in a text __by random chance alone__.
<br>
```python
comb(  # number of combinations
    count_of_ways_to_intersect_n_occurences_of_kmer_with_text_length
    + kmer_occurrence_count,
    kmer_occurrence_count,
)
* pow(
    self.alphabet_size,
    count_of_ways_to_intersect_n_occurences_of_kmer_with_text_length,
)
/ pow(self.alphabet_size, text_length)
```


<br>Here's [the Python version](https://github.com/engelanna/verifying-sars-cov-2-origin-hypotheses/blob/master/src/probabilities/probability_of_kmer_occurring_n_times_in_text.py#L14-L23) should you prefer it to mathematical gobbledygook. Giving it a spin:

https://www.citizensjournal.us/patents-prove-sars-cov-2-is-a-manufactured-virus/
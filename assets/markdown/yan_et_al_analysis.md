---
marp: true
paginate: true
transition: cube
style: |
  section::after {
    content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
  }
---

# Addressing [the Yan report](https://zenodo.org/record/4028830#.X1_bxGhKg2y)

In September 2020, the above claimed to **be** scientific evidence for SARS-CoV-2 being an engineered bioweapon :fearful: Zenodo granting it a Digital Object Identifier (DOI) made the report appear credible, despite a lack of peer review.

<br>The Johns Hopkins University [made up for that lack](https://www.centerforhealthsecurity.org/our-work/pubs_archive/pubs-pdfs/2020/200921-in-response-yan.pdf) the same month, explaining why the report was unconvincing. But conspiratorial audiences :raised_eyebrow::raised_eyebrow: value neither authority, nor being pointed to tonnes of reading material (can't blame them for the latter :smile:).

<br>They do value critical thinking, which only requires that __the core claim__ be verified. Should it prove false, everything else can be dropped :woman_shrugging: What was the report's postulate, then, that sufficed for its authors to be able to seek asylum in :us:?

---

## <!-- fit --> Restriction enzymes around the spike's receptor binding motif

Mikolaj Raszek, PhD, was kind enough to elucidate, in [_SARS-CoV-2 coronavirus origins alternative theories – do they hold up against science?_](https://merogenomics.ca/blog/en/117/SARS-CoV-2_coronavirus_origins_alternative_theories__do_they_hold_up_against_science_Part_2), the core claim of the Yan report.

Two **restriction enzymes** (sequences bacteria use to slash viruses to bits, repurposed by humans to glue parts of different genomes together): [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) and [BstEII](https://www.neb.com/products/r0162-bsteii#Product%20Information). According to Yan et al, the sequence between them allowed to target mammals larger than :bat::bat:.

![Heart of the Yan report](https://user-images.githubusercontent.com/13955209/179063218-748bafb5-5ad1-4f32-a4da-89bd1e3e259f.png)

---

## <!-- fit --> Download the earliest known SARS-CoV-2 genome :arrow_down: (1 of 2)

<br>Yan et al's image caption cites the isolate **Wuhan-Hu-1** (isolate: a population of organisms having little genetic mixing with other organisms of the same species).

<br>![Aaa](https://user-images.githubusercontent.com/13955209/179288273-5f752b8d-1ed1-4a64-bf0d-61e9d792fe59.png)

<br>Viewing [the isolate at _NCBI Virus_](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=Severe%20acute%20respiratory%20syndrome%20coronavirus%202,%20taxid:2697049&IsolateParsed_s=Wuhan-Hu-1), the absolutely earliest accession (unique sequence identifier) is [MN908947.1](https://www.ncbi.nlm.nih.gov/nuccore/MN908947.1), collected in Dec 2019 :arrow_right: submitted 2020-01-05 :arrow_right: released 2020-01-12.

<br>That's 2 months until the World Health Organization would declare COVID-19 a pandemic ☣️ (2020-03-11).

---

## <!-- fit --> Download the earliest known SARS-CoV-2 genome :arrow_down: (2 of 2)

In [the accession page](https://www.ncbi.nlm.nih.gov/nuccore/MN908947.1), switching to the FASTA format (a text format often used for storing reference genomes) allows us to download the troublemaker's genome:

![Downloading](https://user-images.githubusercontent.com/13955209/179091431-050a1882-24e8-4591-b176-d2d905f269aa.png)

~30k bases (a base is one of `A, C, G, T`) long? What a tiny genome. A human one is 3.1 billion bases, with a single cell taking up between 3.3 GB (reference genome, a measurement standard) and 70 GB (non-reference genome) of your hard drive :see_no_evil:

---

## Are EcoRI and BstEII _actually there_? :mag::eyes:

- **Note:** Sequences identical to those listed **needn't** necessarily come from restriction enzymes - but let's simplify and humour that notion :ok_hand::woman:

<br>You can open the downloaded SARS-CoV-2 genome in a text editor :clipboard:, and search (`Ctrl+f` / `Cmd+f`) for the occurrences of the [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) sequence __GAATTC__ yourself. If you fancy a dopamine rush, __stop reading and go ahead now__ :grin:

<br>The __N__ (= whichever base) in [BstEII](https://www.neb.com/products/r0162-bsteii#Product%20Information)'s __GGTNACC__ is a tad more problematic, though. If you can locate _regular expression mode_ (look for a button marked `.*`) :crossed_fingers:, this hurdle can be cleared by inputting __GGT[ACGT]ACC__.

---

## <!-- fit --> Plotting EcoRI & BstEII sequence matches in the spike gene

MN908947.1 spike coordinates | Yan et al's spike coordinates
--------------|:-----:|
![Spike genes](https://user-images.githubusercontent.com/13955209/179913693-f9ab603e-f143-4309-a19e-0f3996dec3dc.png) | ![Heart of the Yan report](https://user-images.githubusercontent.com/13955209/179063218-748bafb5-5ad1-4f32-a4da-89bd1e3e259f.png)

The accession MN908947.1 spike gene **does** contain sequence occurences with 100% identity to EcoRI & BstEII, and that's at the __exact__ coordinates specified by Yan et al :dart: 
So far so good - let's look at the rest of the genome :mag:

---

## <!-- fit --> Plotting EcoRI & BstEII matches across the whole genome

But looking at **all the genes** (instead of just the spike), one seems to find more 'genetic modifications' than Yan et al bargained for :thinking:

There's even an EcoRI match in the 3' untranslated region (nothing there ever becomes live proteins, hence there's no point in engineering the region).


![All genes](https://user-images.githubusercontent.com/13955209/179872222-cb2ecf4a-3f04-4a1e-abb5-1cc1f5e15fad.png)

---

## A restriction enzyme cornucopia? :unicorn: Let's find out :woman_shrugging:

<br>

[_Bioinformatics Algorithms: An Active Learning Approach_](https://bioinformaticsalgorithms.com/faqs/replication.html) gives the formula (search for `approximation`) for approximating the likelihood that a **k-mer** (word of size k) occurs in a text *by random chance alone* :game_die:
<br>
The **lower** :arrow_down: that likelihood, the **more probable** :arrow_up: any bioengineering :dna::scissors::dna: Customarily, values with `< 5%` chance of being randomly generated, are worthy of investigation.
<br>
[Click here](https://github.com/engelanna/verifying-sars-cov-2-origin-hypotheses/blob/master/src/probabilities/probability_of_kmer_occurring_n_times_in_text.py#L14-L23) for the Python version of the approximation formula :snake:. Its code's been [tested](https://github.com/engelanna/verifying-sars-cov-2-origin-hypotheses/blob/main/test/probabilities/test_probability_of_kmer_occurring_n_times_in_text.py), so should be reliable. Let's take it for a spin :yarn::cat:

---

## <!-- fit -->:crossed_swords: Theory vs practice: probabilities along the full genome :dna:

:one: A nice property of our approximation formula: if we seek the probability of **just a single occurrence**, any returned number `> 1.0` is the **expected occurrence count**.

:two: BstEII's middle character  (GGT**N**ACC) can be anything, so BstEII is considered to have length 6 (the same length as EcoRI), instead of 7.

| Restriction enzyme | Expected occurrences | Actual occurrences |
|-:|-:|:-|
| EcoRI (**GAATTC**) | 7.44 | 9 (_...are Yan et al onto something?_)
| BstEII (**GGT_ACC**) | 7.44 | 4 (_...no they aren't_)

No conclusive evidence either way yet :woman_shrugging: Let's concentrate on the spike :eyes:

---

## Occurrence probabilities within the spike gene :pushpin:

[The accession page](https://www.ncbi.nlm.nih.gov/nuccore/MN908947.1) informs us that the range of the `"S"` gene is `21579..25400`, which makes for a length of `3821`. Plugging this text length into our formula :electric_plug:, we get:

```python
In [3]: ProbabilityOfKmerOccurringNTimesInText(alphabet_size=4)(
    ...:     text_length=3821, kmer_length=6, kmer_occurrence_count=1
    ...: )
Out[3]: 0.931640625
```

There's a 93% probability of at least one sequence of length 6 (doesn't matter if it's EcoRI or BstEII) occurring, in a coronavirus spike gene of that length, just by random chance alone. How about the **joint probability of both of them occurring at once**? :point_down::eyes:

---

## Conclusion :unlock: :key:

Since BstEII and EcoRI are considered the same length (after disregarding BstEII's arbitrary middle character, they're each 6 bases long), the joint probability of them occurring together in the spike is approximately `93% * 93%`:

```python
In [4]: 0.931640625 * 0.931640625
Out[4]: 0.8679542541503906
```

:arrow_right: about **87% of all coronaviruses** are going to have - in their spike protein gene - an EcoRI sequence occurring  together with a BstEII sequence. Without the need for **any** genetic engineering :woman_shrugging:

Putting it differently: if SARS-CoV-2 was bioengineered :scissors::dna: the way Yan et al suggested, then 17 in 20 coronaviruses occurring in nature **also were**. Why go through the trouble of bioengineering, when nature has already done the work:question:
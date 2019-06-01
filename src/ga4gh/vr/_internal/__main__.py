"""ga4gh.vr debugging shell

Invoke like this:
ipython -m ga4gh.vr._internal -i

"""


from .. import __version__
from . import *
from .identify import _dictify


print("############################################################################")
print(__package__, __version__)


text = models.Text(definition="PTEN loss")
 
simple_interval = models.SimpleInterval(start=42, end=43)
sequence_location_si = models.SequenceLocation(
    sequence_id="refseq:NM_000551.3",
    interval=simple_interval)
#sequence_location_si.id = computed_id(sequence_location_si)
 
nested_interval = models.NestedInterval(
    inner=models.SimpleInterval(start=29,end=30),
    outer=models.SimpleInterval(start=30,end=39))
sequence_location_ni = models.SequenceLocation(
    sequence_id="refseq:NM_000551.3",
    interval=nested_interval)
 
sequence_state = models.SequenceState(sequence="A")
 
allele_si = models.Allele(location=sequence_location_si, state=sequence_state)
#allele_si.id = computed_id(allele_si)
 
# allele_ni.location is not (yet) id'd
allele_ni = models.Allele(location=sequence_location_ni, state=sequence_state)
#allele_ni.id = computed_id(allele_ni)


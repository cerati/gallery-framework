from .hit import hit
# import match
from .shower import shower
from .track import track
from .wire import wire
from .cluster import cluster
#from .endpoint2d import endpoint2d
from .vertex import vertex
from .mctrack import mctrack
#from .mcshower import mcshower
from .spacepoint import spacepoint
#from .simch import simch
#from .opflash import opflash
#from .seed import seed
#from .pfpart import pfpart
#import neutrino
from .numuselection import numuselection
from .cosmictag import cosmictag
from .t0 import t0

# This is the class that maintains the list of drawable items.
# If your class isn't here, it can't be drawn
import collections


class drawableItems(object):

    """This class exists to enumerate the drawableItems"""
    # If you make a new drawing class, add it here

    def __init__(self):
        super(drawableItems, self).__init__()
        # items are stored as pointers to the classes (not instances)
        self._drawableClasses = collections.OrderedDict()
        self._drawableClasses.update({'Hit': [hit,"recob::Hit"]})
        self._drawableClasses.update({'Cluster': [cluster,"recob::Cluster"]})
        # self._drawableClasses.update({'Match': [match.match,"pfpart"]})
        self._drawableClasses.update({'Shower': [shower,"recob::Shower"]})
        self._drawableClasses.update({'Track': [track,"recob::Track"]})
        self._drawableClasses.update({'MCTrack': [mctrack,"simb::MCParticle"]})
        # # self._drawableClasses.update({'Neutrino': [neutrino.neutrino,"ass"]})
        #self._drawableClasses.update({'Endpoint 2D': [endpoint2d.endpoint2d,"recob::EndPoint2D"]})
        self._drawableClasses.update({'Vertex': [vertex,"recob::Vertex"]})
        self._drawableClasses.update({'SPS': [spacepoint,"recob::SpacePoint"]})
        #self._drawableClasses.update({'Numu Selection': [numuselection.numuselection, "recob::Trackrecob::Vertexvoidart::Assn"]})
        self._drawableClasses.update({'Neutrino Slice': [numuselection, "recob::PFParticle"]})
        self._drawableClasses.update({'Cosmic Tag': [cosmictag, "anab::CosmicTag"]})
        self._drawableClasses.update({'T0 Tag': [t0, "anab::T0"]})

    def getListOfTitles(self):
        return self._drawableClasses.keys()

    def getListOfItems(self):
        return zip(*self._drawableClasses.values())[1]

    def getDict(self):
        return self._drawableClasses


try:
    import pyqtgraph.opengl as gl
    class drawableItems3D(object):

        """This class exists to enumerate the drawableItems in 3D"""
        # If you make a new drawing class, add it here

        def __init__(self):
            super(drawableItems3D, self).__init__()
            # items are stored as pointers to the classes (not instances)
            self._drawableClasses = collections.OrderedDict()
            self._drawableClasses.update({'Spacepoints': [spacepoint.spacepoint3D,"recob::SpacePoint"]})
            self._drawableClasses.update({'PFParticle': [pfpart.pfpart3D,"recob::PFParticle"]})
            self._drawableClasses.update({'Seed': [seed.seed3D,"recob::Seed"]})
            self._drawableClasses.update({'Vertex': [vertex.vertex3D,"recob::Vertex"]})
            self._drawableClasses.update({'Shower': [shower.shower3D,"recob::Shower"]})
            self._drawableClasses.update({'Track': [track.track3D,"recob::Track"]})
            self._drawableClasses.update({'Opflash': [opflash.opflash3D,"recob::OpFlash"]})
            self._drawableClasses.update({'MCTrack': [mctrack.mctrack3D,"sim::MCTrack"]})
            self._drawableClasses.update({'MCShower': [mcshower.mcshower3D,"sim::MCShower"]})
            self._drawableClasses.update({'Simch': [simch.simch3D,"sim::SimChannel"]})

        def getListOfTitles(self):
            return self._drawableClasses.keys()

        def getListOfItems(self):
            return zip(*self._drawableClasses.values())[1]

        def getDict(self):
            return self._drawableClasses



except:
    pass


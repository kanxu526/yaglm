from ya_glm.glm_loss.linear_regression import LinRegMixin

from ya_glm.pen_glms.GlmVanilla import GlmVanilla

from ya_glm.pen_glms.GlmRidge import GlmRidge, GlmRidgeCVPath

from ya_glm.pen_glms.GlmLasso import GlmLasso, GlmLassoCVPath, GlmENet, \
    GlmENetCVPath

from ya_glm.pen_glms.GlmAdaptiveLasso import GlmAdaptiveLasso,\
    GlmAdaptiveLassoCVPath, GlmAdaptiveENet, GlmAdaptiveENetCVPath

from ya_glm.pen_glms.GlmFcpLLA import GlmFcpLLA, GlmFcpLLACV

from ya_glm.init_signature import add_from_classes

from .glm_solver import solve_glm, solve_glm_path
from .WL1SolverGlm import WL1SolverGlm


##############
# Single fit #
##############


class Vanilla(LinRegMixin, GlmVanilla):
    solve_glm = staticmethod(solve_glm)


class Ridge(LinRegMixin, GlmRidge):
    solve_glm = staticmethod(solve_glm)


class Lasso(LinRegMixin, GlmLasso):
    solve_glm = staticmethod(solve_glm)


class ENet(LinRegMixin, GlmENet):
    solve_glm = staticmethod(solve_glm)


class AdaptiveLasso(LinRegMixin, GlmAdaptiveLasso):
    solve_glm = staticmethod(solve_glm)

    def _get_defualt_init(self):
        est = Lasso(**self._kws_for_default_init())
        return LassoCV(estimator=est)


class AdaptiveENet(LinRegMixin, GlmAdaptiveENet):
    solve_glm = staticmethod(solve_glm)

    def _get_defualt_init(self):
        est = ENet(**self._kws_for_default_init())
        return ENetCV(estimator=est)


class FcpLLA(LinRegMixin, GlmFcpLLA):
    solve_glm = staticmethod(solve_glm)
    WL1Solver = WL1SolverGlm

    def _get_defualt_init(self):
        est = Lasso(**self._kws_for_default_init())
        return LassoCV(estimator=est)

####################
# Cross-validation #
####################


class RidgeCV(GlmRidgeCVPath):
    solve_glm_path = staticmethod(solve_glm_path)

    @add_from_classes(GlmRidgeCVPath)
    def __init__(self, estimator=Ridge()): pass


class LassoCV(GlmLassoCVPath):
    solve_glm_path = staticmethod(solve_glm_path)

    @add_from_classes(GlmLassoCVPath)
    def __init__(self, estimator=Lasso()): pass


class ENetCV(GlmENetCVPath):
    solve_glm_path = staticmethod(solve_glm_path)

    @add_from_classes(GlmENetCVPath)
    def __init__(self, estimator=ENet()): pass


class AdaptiveLassoCV(GlmAdaptiveLassoCVPath):
    solve_glm_path = staticmethod(solve_glm_path)

    @add_from_classes(GlmAdaptiveLassoCVPath)
    def __init__(self, estimator=AdaptiveLasso()): pass


class AdaptiveENetCV(GlmAdaptiveENetCVPath):
    solve_glm_path = staticmethod(solve_glm_path)

    @add_from_classes(GlmAdaptiveENetCVPath)
    def __init__(self, estimator=AdaptiveENet()): pass


class FcpLLACV(GlmFcpLLACV):

    @add_from_classes(GlmFcpLLACV)
    def __init__(self, estimator=FcpLLA()): pass

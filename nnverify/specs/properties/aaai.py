import torch

from math import pi

from nnverify import util
from nnverify.specs import spec
from nnverify.common.dataset import Dataset
from nnverify.specs.property import Property, InputSpecType, OutSpecType
from nnverify.specs.out_spec import Constraint


def get_aaai_spec(id):
    """
    get the list of specification mat and const

    @mat and @const
    The verification problem is reduced to proving: (mat * Y + const) >= 0
    """

    # labels = ['Clear of Conflict (COC)', 'Weak Left', 'Weak Right', 'Strong Left', 'Strong Right']
    if id == 1:
        _ = 'safe if Strong Right is minimal'
        init_lb, init_ub = get_init_bounds([-0.00234375000, -0.00234375000, -0.00234375000,-0.00234375000,-0.00234375000],
                                           [0.00234375000, 0.00234375000, 0.00234375000, 0.00234375000, 0.00234375000])
        mat = [
               [0, 0, -1, 0, 1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)

    elif id == 2:
        init_lb, init_ub = get_init_bounds([0.1191666579, 0.1359881419, -0.6660083626,-0.1664062500,-0.1664062500],
                                           [0.4519791579, 0.4688006419, -0.3331958626, 0.1664062500, 0.1664062500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 3:
        init_lb, init_ub = get_init_bounds([0.3398437500, -0.3401562500, -0.5101562500, 0.0098437500, 0.2198437500],
                                           [0.5601562500, -0.1198437500, -0.2898437500, 0.2301562500, 0.4401562500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 4:
        init_lb, init_ub = get_init_bounds([-0.2554687500, -0.3054687500, -0.5554687500, -0.3554687500, -0.4954687500],
                                           [-0.1445312500, -0.1945312500, -0.4445312500, -0.2445312500, -0.3845312500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 5:
        init_lb, init_ub = get_init_bounds([0.5435937500, 0.2935937500, -0.0664062500, -0.0664062500, -0.3064062500],
                                           [0.6764062500, 0.4264062500, 0.0664062500, 0.0664062500, -0.1735937500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 13:
        init_lb, init_ub = get_init_bounds([0.1070312500, 0.1070312500, 0.1070312500, 0.1070312500, 0.1070312500],
                                           [0.3929687500, 0.3929687500, 0.3929687500, 0.3929687500, 0.3929687500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 15:
        init_lb, init_ub = get_init_bounds([0.2273437500, -0.2526562500, -0.4226562500, -0.1026562500, 0.1073437500],
                                           [0.4726562500, -0.0073437500, -0.1773437500, 0.1426562500, 0.3526562500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 16:
        init_lb, init_ub = get_init_bounds([-0.3692187500, -0.2192187500, -0.5992187500, -0.2992187500, -0.5292187500],
                                           [-0.2707812500, -0.1207812500, -0.5007812500, -0.2007812500, -0.4307812500])
        mat = [
               [0, 0, -1, 0, 1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 17:
        init_lb, init_ub = get_init_bounds([-0.3692187500, -0.2192187500, -0.5992187500, -0.2992187500, -0.5292187500],
                                           [-0.2707812500, -0.1207812500, -0.5007812500, -0.2007812500, -0.4307812500])
        mat = [
               [0, 0, -1, 0, 1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 18:
        init_lb, init_ub = get_init_bounds([0.0229687500, 0.0229687500, 0.0229687500, 0.0229687500, 0.0229687500],
                                           [0.0370312500, 0.0370312500, 0.0370312500, 0.0370312500, 0.0370312500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 19:
        init_lb, init_ub = get_init_bounds([-0.0523437500, 0.0476562500, -0.0523437500, 0.0476562500, -0.0323437500],
                                           [-0.0476562500, 0.0523437500, -0.0476562500, 0.0523437500, -0.0276562500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 20:
        init_lb, init_ub = get_init_bounds([0.2263165964, 0.2531775959, -0.5988212053, -0.0555844200, -0.3282156400],
                                           [0.6247540964, 0.6516150959, -0.2003837053, 0.3428530800, 0.0702218600])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 21:
        init_lb, init_ub = get_init_bounds([-0.0223951965, 0.0844257047, -0.7840032920, -0.3223030800, -0.0215232960],
                                           [0.3135423035, 0.4203632047, -0.4480657920, 0.0136344200, 0.3144142040])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 22:
        init_lb, init_ub = get_init_bounds([0.5030062500, 0.2545895500, -0.1381277500, -0.0758872900, -0.3912970395],
                                           [0.7076937500, 0.4592770500, 0.0665597500, 0.1288002100, -0.1866095395])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 23:
        init_lb, init_ub = get_init_bounds([0.5739137500, 0.3228237500, -0.0176762500, 0.0007237500, -0.2414062500],
                                           [0.6567262500, 0.4056362500, 0.0651362500, 0.0835362500, -0.1585937500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 24:
        init_lb, init_ub = get_init_bounds([0.5364137500, 0.2853237500, -0.1026362500, -0.1210362500, -0.2789062500],
                                           [0.6942262500, 0.4431362500, 0.0551762500, 0.0367762500, -0.1210937500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 25:
        init_lb, init_ub = get_init_bounds([0.5739137500, 0.3158237500, -0.0176762500, 0.0007237500, -0.2414062500],
                                           [0.6567262500, 0.3986362500, 0.0651362500, 0.0835362500, -0.1585937500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 26:
        init_lb, init_ub = get_init_bounds([0.5364137500, 0.2803237500, -0.0551762500, -0.0367762500, -0.3646921500],
                                           [0.6942262500, 0.4381362500, 0.1026362500, 0.1210362500, -0.2068796500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 27:
        init_lb, init_ub = get_init_bounds([0.4574132500, 0.2150112500, -0.4829487500, -0.1913487500, -0.3850046500],
                                           [0.7558507500, 0.5134487500, -0.1845112500, 0.1070887500, -0.0865671500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 28:
        init_lb, init_ub = get_init_bounds([0.0304687500, 0.0304687500, 0.0304687500, 0.0304687500, 0.0304687500],
                                           [0.1695312500, 0.1695312500, 0.1695312500, 0.1695312500, 0.1695312500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 31:
        init_lb, init_ub = get_init_bounds([-0.1539062500, 0.0460937500, 0.0460937500, -0.1539062500, -0.1539062500],
                                           [-0.0460937500, 0.1539062500, 0.1539062500, -0.0460937500, -0.0460937500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 33:
        init_lb, init_ub = get_init_bounds([0.0929687500, -0.1070312500, 0.0929687500, 0.0929687500, -0.1070312500],
                                           [0.1070312500, -0.0929687500, 0.1070312500, 0.1070312500, -0.0929687500])
        mat = [
               [0, 0, 1, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 34:
        init_lb, init_ub = get_init_bounds([-0.1179687500, 0.0820312500, -0.1179687500, 0.0820312500, 0.0820312500],
                                           [-0.0820312500, 0.1179687500, -0.0820312500, 0.1179687500, 0.1179687500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    elif id == 35:
        init_lb, init_ub = get_init_bounds([-0.1117187500, -0.1117187500, 0.0882812500, -0.1117187500, -0.1117187500],
                                           [-0.0882812500, -0.0882812500, 0.1117187500, -0.0882812500, -0.0882812500])
        mat = [
               [1, 0, 0, 0, -1]]
        const \
            = [0]
        mat, const \
            = get_out_constr(mat, const)

        out_spec = Constraint(OutSpecType.GLOBAL, constr_mat=(mat, const)
                              )
        return Property([init_lb], [init_ub], InputSpecType.GLOBAL, [out_spec], Dataset.AAAI)
    else:
        raise ValueError("Property not yer supported: ", id)
    


def get_out_constr(mat, const)\
        :
    mat = torch.tensor(mat).type(torch.float).T
    const \
        = torch.tensor(const)

    return mat, const



def get_init_bounds(init_lb, init_ub):
    init_lb = torch.tensor(init_lb).T
    init_ub = torch.tensor(init_ub).T
    mean, std = util.get_mean_std(Dataset.AAAI)
    mean, std = mean.flatten(), std.flatten()
    init_lb = (init_lb - mean) / std
    init_ub = (init_ub - mean) / std
    return init_lb, init_ub
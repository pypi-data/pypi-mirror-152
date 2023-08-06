from pathlib import Path

import pytest
import sympy

from pharmpy import Model
from pharmpy.modeling import (
    convert_model,
    copy_model,
    create_joint_distribution,
    fix_parameters,
    fix_parameters_to,
    generate_model_code,
    get_model_covariates,
    get_omegas,
    get_sigmas,
    get_thetas,
    load_example_model,
    read_model,
    read_model_from_string,
    remove_unused_parameters_and_rvs,
    set_name,
    unfix_parameters,
    unfix_parameters_to,
    write_model,
)


def test_read_model(testdata):
    model = read_model(testdata / 'nonmem' / 'minimal.mod')
    assert model.parameters['THETA(1)'].init == 0.1
    model2 = read_model(str(testdata / 'nonmem' / 'minimal.mod'))
    assert model2.parameters['THETA(1)'].init == 0.1


def test_read_model_from_string(testdata):
    model = read_model_from_string(
        """$PROBLEM base model
$INPUT ID DV TIME
$DATA file.csv IGNORE=@

$PRED
Y = THETA(1) + ETA(1) + ERR(1)

$THETA 0.1
$OMEGA 0.01
$SIGMA 1
$ESTIMATION METHOD=1 INTER MAXEVALS=9990 PRINT=2 POSTHOC
"""
    )
    assert model.parameters['THETA(1)'].init == 0.1


def test_write_model(testdata, tmp_path):
    model = read_model(testdata / 'nonmem' / 'minimal.mod')
    write_model(model, tmp_path / 'run1.mod')
    assert Path(tmp_path / 'run1.mod').is_file()


def test_fix_parameters(testdata):
    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    assert not model.parameters['THETA(1)'].fix
    fix_parameters(model, ['THETA(1)'])
    assert model.parameters['THETA(1)'].fix

    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    assert not model.parameters['THETA(1)'].fix
    fix_parameters(model, 'THETA(1)')
    assert model.parameters['THETA(1)'].fix


def test_unfix_parameters(testdata):
    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters(model, ['THETA(1)'])
    assert model.parameters['THETA(1)'].fix
    unfix_parameters(model, ['THETA(1)'])
    assert not model.parameters['THETA(1)'].fix

    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters(model, 'THETA(1)')
    assert model.parameters['THETA(1)'].fix
    unfix_parameters(model, 'THETA(1)')
    assert not model.parameters['THETA(1)'].fix


def test_fix_parameters_to(testdata):
    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters_to(model, 'THETA(1)', 0)
    assert model.parameters['THETA(1)'].fix
    assert model.parameters['THETA(1)'].init == 0

    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters_to(model, ['THETA(1)', 'OMEGA(1,1)'], 0)
    assert model.parameters['THETA(1)'].fix
    assert model.parameters['THETA(1)'].init == 0
    assert model.parameters['THETA(1)'].fix
    assert model.parameters['OMEGA(1,1)'].init == 0

    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters_to(model, ['THETA(1)', 'OMEGA(1,1)'], [0, 1])
    assert model.parameters['THETA(1)'].init == 0
    assert model.parameters['OMEGA(1,1)'].init == 1

    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters_to(model, None, 0)
    assert all(p.fix for p in model.parameters)
    assert all(p.init == 0 for p in model.parameters)

    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    with pytest.raises(ValueError, match='Incorrect number of values'):
        fix_parameters_to(model, ['THETA(1)', 'OMEGA(1,1)'], [0, 0, 0])

    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters_to(model, None, float(0))
    assert model.parameters['THETA(1)'].fix
    assert model.parameters['THETA(1)'].init == 0


def test_unfix_parameters_to(testdata):
    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters(model, ['THETA(1)'])
    assert model.parameters['THETA(1)'].fix
    unfix_parameters_to(model, 'THETA(1)', 0)
    assert not model.parameters['THETA(1)'].fix
    assert model.parameters['THETA(1)'].init == 0

    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters(model, ['THETA(1)', 'OMEGA(1,1)'])
    assert model.parameters['THETA(1)'].fix
    assert model.parameters['OMEGA(1,1)'].fix
    unfix_parameters_to(model, ['THETA(1)', 'OMEGA(1,1)'], 0)
    assert not model.parameters['THETA(1)'].fix
    assert not model.parameters['OMEGA(1,1)'].fix
    assert model.parameters['THETA(1)'].init == 0
    assert model.parameters['OMEGA(1,1)'].init == 0

    unfix_parameters_to(model, None, values=[1, 2, 3])


def test_generate_model_code(testdata):
    model = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    fix_parameters(model, ['THETA(1)'])
    assert generate_model_code(model).split('\n')[7] == '$THETA 0.1 FIX'


def test_load_example_model():
    model = load_example_model("pheno")
    assert len(model.parameters) == 6
    assert len(model.modelfit_results.parameter_estimates) == 6

    with pytest.raises(ValueError):
        load_example_model("grekztalb23=")


def test_get_model_covariates(pheno, testdata):
    assert set(get_model_covariates(pheno)) == {sympy.Symbol('WGT'), sympy.Symbol('APGR')}
    minimal = Model.create_model(testdata / 'nonmem' / 'minimal.mod')
    assert set(get_model_covariates(minimal)) == set()


def test_set_name(pheno):
    model = pheno.copy()
    set_name(model, "run1")
    assert model.name == "run1"


def test_copy_model(pheno):
    run1 = copy_model(pheno)
    assert id(pheno) != id(run1)
    assert id(pheno.parameters) != id(run1.parameters)
    run2 = copy_model(run1, "run2")
    assert run2.name == "run2"
    assert run2.parent_model == "pheno_real"


def test_convert_model():
    model = load_example_model("pheno")
    run1 = convert_model(model, "nlmixr")
    assert model.name == run1.name
    assert model == run1


def test_remove_unused_parameters_and_rvs(pheno):
    model = pheno.copy()
    remove_unused_parameters_and_rvs(model)
    create_joint_distribution(model)
    statements = model.statements
    i = statements.index(statements.find_assignment('CL'))
    del model.statements[i]
    remove_unused_parameters_and_rvs(model)
    assert not model.random_variables['ETA(2)'].joint_names


def test_get_thetas(pheno):
    thetas = get_thetas(pheno)
    assert len(thetas) == 3
    assert thetas['THETA(1)'].init == 0.00469307


def test_get_omegas(pheno):
    omegas = get_omegas(pheno)
    assert len(omegas) == 2
    assert omegas['OMEGA(1,1)'].init == 0.0309626


def test_get_sigmas(pheno):
    sigmas = get_sigmas(pheno)
    assert len(sigmas) == 1
    assert sigmas['SIGMA(1,1)'].init == 0.013241

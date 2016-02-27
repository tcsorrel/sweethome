# in_venv is a launcher of command within a Python virtualenv
# usage:
#  $ in_venv <vitual env name> <command to launch>
#  $ in_venv TOX tox
#  $ in_venv TOX tox -e py34 -r
#  $ in_venv dev python -m pdb my_app.py
in_venv(){
    (
        VENV=$1
        shift
        . ${WORKON_HOME:-${HOME}/.virtualenvs}/${VENV}/bin/activate
        $*
    )
}

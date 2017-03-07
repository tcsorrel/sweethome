# in-venv is a launcher of command within a Python virtualenv
# usage:
#  $ in-venv <vitual env name> <command to launch>
#  $ in-venv TOX tox
#  $ in-venv TOX tox -e py34 -r
#  $ in-venv dev python -m pdb my_app.py
in-venv(){
    (
        VENV=$1
        shift
        . ${WORKON_HOME:-${HOME}/.virtualenvs}/${VENV}/bin/activate
        $*
    )
}

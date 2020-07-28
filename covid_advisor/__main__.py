import sys
sys.path.append("..")

from covid_advisor.app.advisory_flask import app
app.port = 5000
app.run(host='0.0.0.0')
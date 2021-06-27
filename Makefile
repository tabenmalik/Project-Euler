# Run all tests
.PHONY: test
test: test-units test-accept


# Run only acceptance tests
.PHONY: test-accept
test-accept:
	pytest -v -n 4 tests/test_euler_solutions.py


# Run only unit tests
.PHONY: test-units
test-units:
	pytest -v -n 4 --ignore tests/test_euler_solutions.py


# Clean up ignored files
.PHONY: clean
clean:
	rm -rf project_euler.egg-info
	find . -name *.pyc | xargs rm -f
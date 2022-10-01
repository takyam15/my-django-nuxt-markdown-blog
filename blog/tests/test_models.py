class TestTag:

    def test_display(self, tag):
        assert tag.display() == '#' + tag.name

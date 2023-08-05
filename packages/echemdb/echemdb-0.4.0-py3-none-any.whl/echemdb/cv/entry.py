r"""
A Data Package decribing a Cyclic Voltammogram.

These are the individual elements of a :class:`Database`.

EXAMPLES:

Data Packages containing published data,
also contain information on the source of the data.::

    >>> from echemdb.cv.database import Database
    >>> db = Database.create_example()
    >>> entry = db['alves_2011_electrochemistry_6010_f1a_solid']
    >>> entry.bibliography  # doctest: +NORMALIZE_WHITESPACE +REMOTE_DATA
    Entry('article',
      fields=[
        ('title', 'Electrochemistry at Ru(0001) in a flowing CO-saturated electrolyte—reactive and inert adlayer phases'),
        ('journal', 'Physical Chemistry Chemical Physics'),
        ('volume', '13'),
        ('number', '13'),
        ('pages', '6010--6021'),
        ('year', '2011'),
        ('publisher', 'Royal Society of Chemistry'),
        ('abstract', 'We investigated ...')],
      persons=OrderedCaseInsensitiveDict([('author', [Person('Alves, Otavio B'), Person('Hoster, Harry E'), Person('Behm, Rolf J{\\"u}rgen')])]))

"""
# ********************************************************************
#  This file is part of echemdb.
#
#        Copyright (C) 2021-2022 Albert Engstfeld
#        Copyright (C)      2021 Johannes Hermann
#        Copyright (C) 2021-2022 Julian Rüth
#        Copyright (C)      2021 Nicolas Hörmann
#
#  echemdb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  echemdb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with echemdb. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************
import logging
import os.path

from echemdb.cv.descriptor import Descriptor

logger = logging.getLogger("echemdb")


class Entry:
    r"""
    A [data packages](https://github.com/frictionlessdata/datapackage-py)
    describing a Cyclic Voltammogram.

    EXAMPLES:

    Entries could be created directly from a datapackage that has been created
    with svgdigitizer's `cv` command. However, they are normally obtained by
    opening a :class:`Database` of entries::

        >>> from echemdb.cv.database import Database
        >>> database = Database.create_example()
        >>> entry = next(iter(database))

    """

    def __init__(self, package, bibliography):
        self.package = package
        self.bibliography = bibliography

    @property
    def identifier(self):
        r"""
        Return a unique identifier for this entry, i.e., its filename in the echemdb.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry.identifier
            'alves_2011_electrochemistry_6010_f1a_solid'

        """
        return self.package.resources[0].name

    def __dir__(self):
        r"""
        Return the attributes of this entry.

        Implement to support tab-completion into the data package's descriptor.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> dir(entry) # doctest: +NORMALIZE_WHITESPACE
            ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
            '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__',
            '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
            '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
            '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
            '__subclasshook__', '__weakref__',
            '_descriptor', '_digitize_example', '_normalize_field_name',
            'bibliography', 'citation', 'create_examples', 'curation', 'data_description',
            'df', 'experimental', 'field_unit', 'figure_description',
            'identifier', 'package', 'plot', 'profile', 'rescale',
            'resources', 'source', 'system', 'thumbnail', 'version', 'yaml']

        """
        return list(set(dir(self._descriptor) + object.__dir__(self)))

    def __getattr__(self, name):
        r"""
        Return a property of the data package's descriptor.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry.source # doctest: +NORMALIZE_WHITESPACE
            {'citation key': 'alves_2011_electrochemistry_6010',
            'url': 'https://doi.org/10.1039/C0CP01001D',
            'version': 1, 'figure': '1a', 'curve': 'solid'}

        The returned descriptor can again be accessed in the same way::

            >>> entry.system.electrolyte.components[0].name
            'H2O'

        """
        return getattr(self._descriptor, name)

    def __getitem__(self, name):
        r"""
        Return a property of the data package's descriptor.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry["source"] # doctest: +NORMALIZE_WHITESPACE
            {'citation key': 'alves_2011_electrochemistry_6010',
            'url': 'https://doi.org/10.1039/C0CP01001D',
            'version': 1, 'figure': '1a', 'curve': 'solid'}

        """
        return self._descriptor[name]

    @property
    def _descriptor(self):
        return Descriptor(self.package.to_dict())

    def citation(self, backend="text"):
        r"""
        Return a formatted reference for the entry's bibliography such as:

        J. Doe, et al., Journal Name, volume (YEAR) page, "Title"

        Rendering default is plain text 'text', but can be changed to any format
        supported by pybtex, such as markdown 'md', 'latex' or 'html'.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry.citation(backend='text')
            'O. B. Alves et al. Electrochemistry at Ru(0001) in a flowing CO-saturated electrolyte—reactive and inert adlayer phases. Physical Chemistry Chemical Physics, 13(13):6010–6021, 2011.'
            >>> print(entry.citation(backend='md'))
            O\. B\. Alves *et al\.*
            *Electrochemistry at Ru\(0001\) in a flowing CO\-saturated electrolyte—reactive and inert adlayer phases*\.
            *Physical Chemistry Chemical Physics*, 13\(13\):6010–6021, 2011\.

        """
        from pybtex.style.formatting.unsrt import Style

        # TODO:: Remove `class EchemdbStyle` from citation and improve citation style. (see #104)
        class EchemdbStyle(Style):
            r"""
            A citation style for the echemdb website.
            """

            def format_names(self, role, as_sentence=True):
                from pybtex.style.template import node

                @node
                def names(_, context, role):
                    persons = context["entry"].persons[role]
                    style = context["style"]

                    names = [
                        style.format_name(person, style.abbreviate_names)
                        for person in persons
                    ]

                    if len(names) == 1:
                        return names[0].format_data(context)

                    from pybtex.style.template import tag, words

                    # pylint: disable=no-value-for-parameter
                    return words(sep=" ")[names[0], tag("i")["et al."]].format_data(
                        context
                    )

                # pylint: disable=no-value-for-parameter
                names = names(role)

                from pybtex.style.template import sentence

                return sentence[names] if as_sentence else names

            def format_title(self, e, which_field, as_sentence=True):
                from pybtex.style.template import field, sentence, tag

                # pylint: disable=no-value-for-parameter
                title = tag("i")[field(which_field)]
                return sentence[title] if as_sentence else title

        return (
            EchemdbStyle(abbreviate_names=True)
            .format_entry("unused", self.bibliography)
            .text.render_as(backend)
        )

    def field_unit(self, field_name):
        r"""
        Return the unit of the ``field_name`` of the ``echemdb`` resource.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry.field_unit('E')
            'V'

        """
        return self.package.get_resource("echemdb").schema.get_field(field_name)["unit"]

    def rescale(self, units=None):
        r"""
        Returns a rescaled :class:`Entry` with axes in the specified ``units``.
        Provide a dict, where the key is the axis name and the value
        the new unit, such as `{'j': 'uA / cm2', 't': 'h'}`.

        EXAMPLES:

        The units without any rescaling::

            >>> entry = Entry.create_examples()[0]
            >>> entry.package.get_resource('echemdb').schema.fields # doctest: +NORMALIZE_WHITESPACE
            [{'name': 't', 'unit': 's', 'type': 'number'},
            {'name': 'E', 'unit': 'V', 'reference': 'RHE', 'type': 'number'},
            {'name': 'j', 'unit': 'A / m2', 'type': 'number'}]

        A rescaled entry using different units::

            >>> rescaled_entry = entry.rescale({'j':'uA / cm2', 't':'h'})
            >>> rescaled_entry.package.get_resource('echemdb').schema.fields # doctest: +NORMALIZE_WHITESPACE
            [{'name': 't', 'unit': 'h', 'type': 'number'},
            {'name': 'E', 'unit': 'V', 'reference': 'RHE', 'type': 'number'},
            {'name': 'j', 'unit': 'uA / cm2', 'type': 'number'}]

        The values in the data frame are scaled to match the new units::

            >>> rescaled_entry.df
                         t         E          j
            0     0.000000 -0.103158 -99.827664
            1     0.000006 -0.102158 -98.176205
            ...

        A rescaled entry with the original axes units of the digitized plot::

            >>> rescaled_entry = entry.rescale(units='original')
            >>> rescaled_entry.package.get_resource('echemdb').schema.fields # doctest: +NORMALIZE_WHITESPACE
            [{'name': 't', 'unit': 's', 'type': 'number'},
            {'name': 'E', 'unit': 'V', 'reference': 'RHE', 'type': 'number'},
            {'name': 'j', 'unit': 'mA / cm2', 'type': 'number'}]

        """
        if units == "original":
            units = {
                field["name"]: field["unit"] for field in self.figure_description.fields
            }

        if not units:
            units = {}

        from copy import deepcopy

        from astropy import units as u

        package = deepcopy(self.package)
        fields = self.package.get_resource("echemdb").schema.fields
        df = self.df.copy()

        for idx, field in enumerate(fields):
            if field.name in units:
                df[field.name] *= u.Unit(field["unit"]).to(u.Unit(units[field.name]))
                package.get_resource("echemdb")["schema"]["fields"][idx][
                    "unit"
                ] = units[field["name"]]

        package.get_resource("echemdb").data = df.to_csv(index=False).encode()

        return Entry(package=package, bibliography=self.bibliography)

    @property
    def df(self):
        r"""
        Return the data of this entry as a data frame.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry.df
                          t         E         j
            0      0.000000 -0.103158 -0.998277
            1      0.020000 -0.102158 -0.981762
            ...

        The units and descriptions of the axes in the data frame can be recovered::

            >>> entry.package.get_resource('echemdb').schema.fields # doctest: +NORMALIZE_WHITESPACE
            [{'name': 't', 'unit': 's', 'type': 'number'},
            {'name': 'E', 'unit': 'V', 'reference': 'RHE', 'type': 'number'},
            {'name': 'j', 'unit': 'A / m2', 'type': 'number'}]

        """
        from io import BytesIO

        import pandas as pd

        return pd.read_csv(BytesIO(self.package.get_resource("echemdb").data))

    def __repr__(self):
        r"""
        Return a printable representation of this entry.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry
            Entry('alves_2011_electrochemistry_6010_f1a_solid')

        """
        return f"Entry({repr(self.identifier)})"

    def _normalize_field_name(self, field_name):
        r"""
        Return a field name when it exists in the `echemdb` resource's field names.

        If 'j' is requested and does not exists in the resource's field names,
        'I' will be returned instead.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry._normalize_field_name('j')
            'j'
            >>> entry._normalize_field_name('x')
            Traceback (most recent call last):
            ...
            ValueError: No axis named 'x' found.

        """
        if field_name in self.package.get_resource("echemdb").schema.field_names:
            return field_name
        if field_name == "j":
            return self._normalize_field_name("I")
        raise ValueError(f"No axis named '{field_name}' found.")

    def thumbnail(self, width=96, height=72, dpi=72, **kwds):
        r"""
        Return a thumbnail of the entry's curve as a PNG byte stream.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry.thumbnail()
            b'\x89PNG...'

        The PNG's ``width`` and ``height`` can be specified in pixels.
        Additional keyword arguments are passed to the data frame plotting
        method::

            >>> entry.thumbnail(width=4, height=2, color='red', linewidth=2)
            b"\x89PNG..."

        """
        kwds.setdefault("color", "b")
        kwds.setdefault("linewidth", 1)
        kwds.setdefault("legend", False)

        import matplotlib.pyplot

        # A reasonable DPI setting that should work for most screens is the default value of 72.
        fig, axis = matplotlib.pyplot.subplots(
            1, 1, figsize=[width / dpi, height / dpi], dpi=dpi
        )
        self.df.plot(
            "E",
            self._normalize_field_name("j"),
            ax=axis,
            **kwds,
        )

        matplotlib.pyplot.axis("off")
        matplotlib.pyplot.close(fig)

        import io

        buffer = io.BytesIO()
        fig.savefig(buffer, format="png", transparent=True, dpi=dpi)

        buffer.seek(0)
        return buffer.read()

    def plot(self, x_label="E", y_label="j"):
        r"""
        Return a plot of this entry.
        The default plot is a cyclic voltammogram ('j vs E').
        When `j` is not defined `I` is used instead.

        EXAMPLES::

            >>> entry = Entry.create_examples()[0]
            >>> entry.plot()
            Figure(...)

        The plot can also be returned with custom axis units available in the resource::

            >>> entry.plot(x_label='t', y_label='E')
            Figure(...)

        The plot with axis units of the original figure can be obtained by first rescaling the entry::

            >>> rescaled_entry = entry.rescale('original')
            >>> rescaled_entry.plot()
            Figure(...)

        """
        import plotly.graph_objects

        x_label = self._normalize_field_name(x_label)
        y_label = self._normalize_field_name(y_label)

        fig = plotly.graph_objects.Figure()

        fig.add_trace(
            plotly.graph_objects.Scatter(
                x=self.df[x_label],
                y=self.df[y_label],
                mode="lines",
                name=f"Fig. {self.source.figure}: {self.source.curve}",
            )
        )

        def reference(label):
            if label == "E":
                return f" vs. {self.package.get_resource('echemdb').schema.get_field(label)['reference']}"

            return ""

        def axis_label(label):
            return f"{label} [{self.field_unit(label)}{reference(label)}]"

        fig.update_layout(
            template="simple_white",
            showlegend=True,
            autosize=True,
            width=600,
            height=400,
            margin=dict(l=70, r=70, b=70, t=70, pad=7),
            xaxis_title=axis_label(x_label),
            yaxis_title=axis_label(y_label),
        )

        fig.update_xaxes(showline=True, mirror=True)
        fig.update_yaxes(showline=True, mirror=True)

        return fig

    @classmethod
    def create_examples(cls, name="alves_2011_electrochemistry_6010"):
        r"""
        Return some example entries for use in automated tests.

        The examples are built on-demand from data in echemdb's examples directory.

        EXAMPLES::

            >>> Entry.create_examples()
            [Entry('alves_2011_electrochemistry_6010_f1a_solid')]

        """
        source = os.path.join(os.path.dirname(__file__), "..", "..", "examples", name)

        if not os.path.exists(source):
            raise ValueError(
                f"No subdirectory in examples/ for {name}, i.e., could not find {source}."
            )

        outdir = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "data",
            "generated",
            "svgdigitizer",
            name,
        )

        cls._digitize_example(source=source, outdir=outdir)

        from echemdb.local import collect_bibliography, collect_datapackages

        packages = collect_datapackages(outdir)
        bibliography = collect_bibliography(source)
        assert len(bibliography) == 1, f"No bibliography found for {name}."
        bibliography = next(iter(bibliography))

        if len(packages) == 0:
            from glob import glob

            raise ValueError(
                f"No literature data found for {name}. The directory for this data {outdir} exists. But we could not find any datapackages in there. "
                f"There is probably some outdated data in {outdir}. The contents of that directory are: { glob(os.path.join(outdir,'**')) }"
            )

        return [
            Entry(package=package, bibliography=bibliography) for package in packages
        ]

    @classmethod
    def _digitize_example(cls, source, outdir):
        r"""
        Digitize ``source`` and write the output to ``outdir``.

        When running tests in parallel, this introduces a race condition that
        we avoid with a global lock in the file system. Therefore, this method
        not is not suitable to digitize files outside of doctesting. To
        digitize data in bulk, have a look at the ``Makefile`` in the
        echemdb/website project.
        """
        lockfile = f"{outdir}.lock"
        os.makedirs(os.path.dirname(lockfile), exist_ok=True)

        from filelock import FileLock

        with FileLock(lockfile):
            if not os.path.exists(outdir):
                from glob import glob

                for yaml in glob(os.path.join(source, "*.yaml")):
                    svg = os.path.splitext(yaml)[0] + ".svg"

                    from svgdigitizer.__main__ import digitize_cv
                    from svgdigitizer.test.cli import invoke

                    invoke(
                        digitize_cv,
                        "--sampling-interval",
                        ".001",
                        "--package",
                        "--metadata",
                        yaml,
                        svg,
                        "--outdir",
                        outdir,
                    )

                assert os.path.exists(
                    outdir
                ), f"Ran digitizer to generate {outdir}. But directory is still missing after invoking digitizer."
                assert any(
                    os.scandir(outdir)
                ), f"Ran digitizer to generate {outdir}. But the directory generated is still empty."

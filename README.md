# RecTable: Convenience for rendering deep recursive structures in HTML.

An example is probably simplest:

```
>>> print rectable.present({'k': '{"json": "value"}', "list": ['a', 'b']})
<table>
  <tr class="key">
    <th>
      k
    </th>
    <td>
      <table class="json">
        <tr class="key">
          <th>
            json
          </th>
          <td>
            value
          </td>
        </tr>
      </table>
    </td>
  </tr>

  <tr class="key">
    <th>
      list
    </th>
    <td>
      <table>
        <tr class="index">
          <th>
            0
          </th>
          <td>
            a
          </td>
        </tr>

        <tr class="index">
          <th>
            1
          </th>
          <td>
            b
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

## API
rectable.present(thing, **kw) returns a string

Understood keyword args are:

<table>
  <thead><tr><th>arg</th><th>default</th></tr></thead>
  <tbody>
    <tr><td>linesep</td><td>'\n'</td></tr>
    <tr><td>indent</td><td>'  ' (that's two spaces)</td></tr>
    <tr><td>parsers</td><td>(('json', json.loads),)</td></tr>
  </tbody>
</table>

It tries to load anyjson, before falling back to json.

## To do

* The tests could be a lot better, especially with respect to custom string
  parsers.

* A default XML-parser/unraveler could be included. The reason it's not is
  that XML is dangerously bad. (Billion laughs, etc.)

* A few things should probably be renamed

* Perhaps long/short form should perhaps be controllable at the th/td level
  separately


## License

The license is the Apache License 2.0.

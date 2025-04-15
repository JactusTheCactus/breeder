i have a `js` script for generating badges, so formatting's fine.
in case you give a shit (unlikely):
```js
function badgeURL([label, colour]) {
    const colours = {
        white: 'fff',
        grey: '888',
        black: '000',
        red: 'f00',
        orange: 'f80',
        yellow: 'ff0',
        green: '0f0',
        blue: '00f',
        purple: '80f',
        pink: 'f0f',
    };
    label = label || 'Badge';
    colour = colour || 'white';
    const hex = colours[colour.toLowerCase()] || 'fff';
    const badgeText = `${encodeURIComponent(label)}-${hex}`;
    return `https://img.shields.io/badge/${badgeText}?style=for-the-badge`;
}
```
how could i modify this for simplicity of integration, and how do i replace the `text`/`tspan`?
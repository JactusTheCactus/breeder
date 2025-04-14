```js
const tspanData = {
    label: [label, "bold", 'normal', 0],
    score: [outgoing - incoming, "normal", "italic", 1]
};
tspanData.forEach(item => {
    tspanFormat(item[0], item[1], item[2], item[3]);
});
```
`tspanData` was a list`[]`, but i changed it to an object`{}`. what do i use instead of `.forEach()`?
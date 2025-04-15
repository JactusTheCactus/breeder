```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Type Chart</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            padding-top: 50px;
            background-color: #fff;
        }

        text {
            font-family: sans-serif;
        }

        line {
            stroke: #888888;
            stroke-width: 2;
        }

        circle {
            fill: #444;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <svg id="chart">
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="#888" />
            </marker>
            <marker id="red-arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="#f00" />
            </marker>
            <marker id="blue-arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="#00f" />
            </marker>
            <marker id="purple-arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="#80f" />
            </marker>
        </defs>
    </svg>
    <script>
        const body = document.body;
        body.setAttribute("font-size", 20);
        const em = body.getAttribute("font-size");
        console.log(`${em}px`);
        const labels = [
            "Fire",
            "Earth",
            "Lightning",
            "Toxic",
            "Water",
            "Undead",
            "Light",
            "Air",
            "Dark"
        ];
        const connections = [
            [0, 7], [4, 0], [6, 8], [8, 6], [4, 1], [2, 1], [3, 7],
            [2, 4], [6, 5], [0, 8], [2, 8], [3, 4], [0, 5], [5, 7]
        ];
        const counts = labels.map(() => ({ incoming: 0, outgoing: 0 }));
        connections.forEach(([source, target]) => {
            counts[source].outgoing += 1;
            counts[target].incoming += 1;
        });
        const svg = document.getElementById("chart");
        svg.setAttribute("width", window.innerWidth);
        svg.setAttribute("height", window.innerHeight);
        const centerX = svg.getAttribute('width') / 2;
        const centerY = svg.getAttribute('height') / 2;
        let radius = Math.min(centerX, centerY) / 2;
        const pointCoords = [];
        const drawnLines = [];
        labels.forEach((label, i) => {
            const angle = (2 * Math.PI / labels.length) * i - Math.PI / 2;
            const x = centerX + radius * Math.cos(angle);
            const y = centerY + radius * Math.sin(angle);
            pointCoords.push({ x, y });
            const labelEl = document.createElementNS("http://www.w3.org/2000/svg", "text");
            labelEl.setAttribute("x", x);
            labelEl.setAttribute("y", y);
            labelEl.setAttribute("text-anchor", "middle");
            // Determine dx/dy offset based on quadrant
            function labelPos(x, y) {
                const offset = 1.5;
                const svgWidth = svg.getAttribute("width");
                const svgHeight = svg.getAttribute("height");
                const dx = x > svgWidth / 2 ? offset : x < svgWidth / 2 ? -offset : 0;
                const dy = y > svgHeight / 2 ? offset : y < svgHeight / 2 ? -offset : 0;
                return { dx, dy };
            }
            // Create tspan element with position offset
            function tspanFormat(text = '', weight = 'normal', style = 'normal', delY = 0) {
                const item = document.createElementNS("http://www.w3.org/2000/svg", "tspan");
                item.textContent = text;
                var { dx, dy } = labelPos(x, y);
                const dyOffset = delY === 0 ? 0 : delY * 2;
                item.setAttribute("font-weight", weight);
                item.setAttribute("font-style", style);
                item.setAttribute("data-point", i);
                item.setAttribute("x", x);
                if (item.getAttribute("font-style") === "italic") {
                    dy = -dy
                }
                item.setAttribute("dx", `${dx}em`);
                item.setAttribute("dy", `${dy}em`);
                labelEl.appendChild(item);
            }
            const incoming = connections.filter(([_, target]) => target === i).length;
            const outgoing = connections.filter(([source]) => source === i).length;
            const tspanData = {
                label: [`${label}`, "bold", 'normal', 0],
                score: [`${outgoing - incoming}`, "normal", "italic", 1]
            };
            Object.values(tspanData).forEach(item => {
                tspanFormat(item[0], item[1], item[2], item[3]);
            });
            labelEl.style.fontSize = '3em';
            svg.appendChild(labelEl);
            const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            circle.setAttribute("cx", x);
            circle.setAttribute("cy", y);
            circle.setAttribute("r", 8);
            circle.setAttribute("data-point", i);
            circle.addEventListener("click", onPointClick);
            svg.appendChild(circle);
        });
        connections.forEach(([a, b]) => {
            const { x: x1, y: y1 } = pointCoords[a];
            const { x: x2, y: y2 } = pointCoords[b];
            const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
            line.setAttribute("x1", x1);
            line.setAttribute("y1", y1);
            line.setAttribute("x2", x2);
            line.setAttribute("y2", y2);
            line.setAttribute("marker-end", "url(#arrow)");
            line.dataset.source = a;
            line.dataset.target = b;
            svg.appendChild(line);
            drawnLines.push(line);
        });
        function onPointClick(e) {
            drawnLines.forEach(line => {
                line.style.stroke = "#888888";
                line.setAttribute("marker-end", "url(#arrow)");
            });
            document.querySelectorAll("text tspan").forEach(tspan => {
                tspan.setAttribute("font-style", "normal");
                tspan.setAttribute('font-size', '1em');
            });
            const clickedIndex = Number(this.getAttribute("data-point"));
            document.querySelectorAll(`text tspan[data-point="${clickedIndex}"]`).forEach(tspan => {
                tspan.setAttribute("font-style", "italic");
                tspan.setAttribute('font-size', '1.5em');
            });
            drawnLines.forEach(line => {
                const source = Number(line.dataset.source);
                const target = Number(line.dataset.target);
                if (source !== clickedIndex && target !== clickedIndex) return;
                const reverseExists = drawnLines.some(l =>
                    Number(l.dataset.source) === target &&
                    Number(l.dataset.target) === source
                );
                if (reverseExists) {
                    line.style.stroke = "#80f";
                    line.setAttribute("marker-end", "url(#purple-arrow)");
                } else {
                    if (source === clickedIndex) {
                        line.style.stroke = "#00f";
                        line.setAttribute("marker-end", "url(#blue-arrow)");
                    } else if (target === clickedIndex) {
                        line.style.stroke = "#f00";
                        line.setAttribute("marker-end", "url(#red-arrow)");
                    }
                }
            });
        }
    </script>
</body>

</html>
```
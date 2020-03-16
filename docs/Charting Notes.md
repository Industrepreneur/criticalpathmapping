# Map Graphing Notes

- Separate Data and Display code
- data/control layer takes in data and preferences and tranforms them into a very simple data structure, which is then passed to the the display layer for rendering (either MAP or PIE.)


## Pie Chart

### Chart Types

1. Value Type Chart
   - Very simple, just calculates % distribution of the three Value Types

1. Operation Type Chart
   - Calculate % distribution, grouping by Operation Types

### Data Structure

    {
        label: 'All Operations by Value Type',
        rows: [
            { label: 'Value Add', background: '#0000CC', icon: 'fa-plus-circle', value: 20 },
            { label: 'Non Value Add', background: '#000088', icon: 'fa-minus-circle', value: 45 },
            { label: 'Required Non Value Add', background: '#000055', icon: 'fa-times-circle' value: 35 }
        ]
    }

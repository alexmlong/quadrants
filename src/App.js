import React, { Component } from 'react';
import {Motion, spring} from 'react-motion';
var json = require("json!./creatures.json");


const App = React.createClass({
  getInitialState() {
    return {
      open: false,
      creatures: [],
    };
  },

  componentDidMount() {
    var self = this;
    setInterval(() => {
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
          var newCreatures = JSON.parse(xhttp.responseText);
          self.setState({creatures: newCreatures.map(newCreature => {
            newCreature.x = newCreature.loc % 3;
            newCreature.y = (newCreature.loc - newCreature.x) / 3;
            return newCreature;
          })});
        }
      };
      xhttp.open("GET", "http://localhost/", true);
      xhttp.send();
    }, 2000);
  },

  handleMouseDown() {
    this.setState({open: !this.state.open});
  },

  getJitter() {
    return Math.floor(Math.random() * 50) + 1;
  },

  render() {
    const randX = Math.floor(Math.random() * 50) + 1;
    const randY = Math.floor(Math.random() * 50) + 1;
    const zeroStyle = {x: spring(0), y: spring(0)};
    const style = {x: spring(randX), y: spring(randY)};
    console.log(this.state.creatures);
    return (
        <div>
          <div>
            <button onClick={this.handleMouseDown}>
              Toggle
            </button>
          </div>
          {this.state.creatures.map(creature => {
            return <Motion style={{x: spring(creature.x * 300 + this.getJitter()), y: spring(creature.y * 300 + this.getJitter())}}>
              {({x, y}) => {
                // children is a callback which should accept the current value of
                // `style`
                return (
                  <div className="creature" style={{
                    position: "absolute",
                    transform: `translate3d(${x}px, ${y}px, 0)`,
                  }}>{creature.id}</div>
                  );
                }
              }
            </Motion>
          })}
        </div>
    );
  }
})

export default App;

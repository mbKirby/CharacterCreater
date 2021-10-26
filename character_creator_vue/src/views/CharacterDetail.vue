<template>
  <div>
    <div class="text-center">
      <p class="fs-2">
        {{ character.name }} Level:{{ character.characterLevel }}
      </p>
      <p class="fs-4">
        Race: {{ character.raceSelection }} SubRace:
        {{ character.subRaceSelection }}
      </p>
      <p class="fs-4">
        Class: {{ character.classSelection }} SubClass:
        {{ character.subClassSelection }}
      </p>
      <p class="fs-4">Alignment: {{ character.alignmentSelection }}</p>
    </div>

    <div class="tect-center">
      <div>AC: {{ character.armorClass }}</div>
      <div>Initiative: {{ savingThrows(character.dex) }}</div>
      <div>Speed {{ character.Speed }}</div>
    </div>

    <div class="row text-center">
      <div class="col border">
        <p>CHA: {{ character.cha }}</p>
        <p>Saving Throw: {{ savingThrows(character.cha) }}</p>
        <div :key="skill" v-for="skill in proficiencies.cha">
          <p
            :key="skillDesc"
            v-for="[skillDesc, skillValue] of Object.entries(skill)"
          >
            {{ skillDesc }}: {{ skillValue + savingThrows(character.cha) }}
          </p>
        </div>
      </div>

      <div class="col border">
        <p>CON: {{ character.con }}</p>
        <p>Saving Throw: {{ savingThrows(character.con) }}</p>
      </div>

      <div class="col border">
        <p>DEX: {{ character.dex }}</p>
        <p>Saving Throw: {{ savingThrows(character.dex) }}</p>
        <div :key="skill" v-for="skill in proficiencies.dex">
          <p
            :key="skillDesc"
            v-for="[skillDesc, skillValue] of Object.entries(skill)"
          >
            {{ skillDesc }}: {{ skillValue + savingThrows(character.dex) }}
          </p>
        </div>
      </div>
    </div>

    <div class="row text-center">
      <div class="col border">
        <p>INT: {{ character.int }}</p>
        <p>Saving Throw: {{ savingThrows(character.int) }}</p>
        <div :key="skill" v-for="skill in proficiencies.int">
          <p
            :key="skillDesc"
            v-for="[skillDesc, skillValue] of Object.entries(skill)"
          >
            {{ skillDesc }}: {{ skillValue + savingThrows(character.int) }}
          </p>
        </div>
      </div>

      <div class="col border">
        <p>STR: {{ character.str }}</p>
        <p>Saving Throw: {{ savingThrows(character.str) }}</p>
        <div :key="skill" v-for="skill in proficiencies.str">
          <p
            :key="skillDesc"
            v-for="[skillDesc, skillValue] of Object.entries(skill)"
          >
            {{ skillDesc }}: {{ skillValue + savingThrows(character.str) }}
          </p>
        </div>
      </div>

      <div class="col border">
        <p>WIS: {{ character.wis }}</p>
        <p>Saving Throw: {{ savingThrows(character.wis) }}</p>
        <div :key="skill" v-for="skill in proficiencies.wis">
          <p
            :key="skillDesc"
            v-for="[skillDesc, skillValue] of Object.entries(skill)"
          >
            {{ skillDesc }}: {{ skillValue + savingThrows(character.wis) }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  props: ["characterName"],
  data() {
    return {
      character: {},
      proficiencies: {
        cha: [
          { Deception: 0 },
          { Intimidation: 0 },
          { Performance: 0 },
          { Persuasion: 0 },
        ],
        con: [],
        dex: [{ Acrobatics: 0 }, { "Sleight of Hand": 0 }, { Stealth: 0 }],
        int: [
          { Arcana: 0 },
          { History: 0 },
          { Investigation: 0 },
          { Nature: 0 },
          { Religion: 0 },
        ],
        str: [{ Athletics: 0 }],
        wis: [
          { "Animal Handling": 0 },
          { Insight: 0 },
          { Medicine: 0 },
          { Perception: 0 },
          { Survival: 0 },
        ],
      },
    };
  },
  methods: {
    getCharacter() {
      axios({
        method: "get",
        url: "http://127.0.0.1:5050/characters/" + `${this.characterName}`,
        headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
      })
        .then((response) => {
          this.character = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    savingThrows(ability) {
      let save = 0;
      switch (ability) {
        case 1:
          save = -5;
          break;
        case 2:
        case 3:
          save = -4;
          break;
        case 4:
        case 5:
          save = -3;
          break;
        case 6:
        case 7:
          save = -2;
          break;
        case 8:
        case 9:
          save = -1;
          break;
        case 10:
        case 11:
          save = 0;
          break;
        case 12:
        case 13:
          save = 1;
          break;
        case 14:
        case 15:
          save = 2;
          break;
        case 16:
        case 17:
          save = 3;
          break;
        case 18:
        case 19:
          save = 4;
          break;
        case 20:
        case 21:
          save = 5;
          break;
        case 22:
        case 23:
          save = 6;
          break;
        case 24:
        case 25:
          save = 7;
          break;
        case 26:
        case 27:
          save = 8;
          break;
        case 28:
        case 29:
          save = 9;
          break;
        case 30:
          save = 10;
      }
      return save;
    },
  },
  mounted() {
    this.getCharacter();
  },
};
</script>
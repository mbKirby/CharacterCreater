<template>
  <div class="container">
    <nav>
      <div class="nav nav-tabs" id="nav-tab" role="tablist">
        <button
          class="nav-link active"
          id="character-tab"
          data-bs-toggle="tab"
          data-bs-target="#character"
          type="button"
          role="tab"
          aria-controls="character"
          aria-selected="true"
        >
          Character
        </button>

        <button
          class="nav-link"
          id="race-tab"
          data-bs-toggle="tab"
          data-bs-target="#race"
          type="button"
          role="tab"
          aria-controls="race"
          aria-selected="false"
        >
          Race
        </button>

        <button
          class="nav-link"
          id="class-tab"
          data-bs-toggle="tab"
          data-bs-target="#class"
          type="button"
          role="tab"
          aria-controls="class"
          aria-selected="false"
        >
          Class
        </button>

        <button
          class="nav-link"
          id="abilityScores-tab"
          data-bs-toggle="tab"
          data-bs-target="#abilityScores"
          type="button"
          role="tab"
          aria-controls="abilityScores"
          aria-selected="false"
        >
          Ability Scores
        </button>

        <button
          class="nav-link"
          id="background-tab"
          data-bs-toggle="tab"
          data-bs-target="#background"
          type="button"
          role="tab"
          aria-controls="background"
          aria-selected="false"
        >
          Background
        </button>

        <button
          class="nav-link"
          id="proficiency-tab"
          data-bs-toggle="tab"
          data-bs-target="#proficiency"
          type="button"
          role="tab"
          aria-controls="proficiency"
          aria-selected="false"
        >
          Proficiencies
        </button>

        <button
          class="nav-link"
          id="spells-tab"
          data-bs-toggle="tab"
          data-bs-target="#spells"
          type="button"
          role="tab"
          aria-controls="spells"
          aria-selected="false"
        >
          Spells
        </button>

        <button
          class="nav-link"
          id="equipment-tab"
          data-bs-toggle="tab"
          data-bs-target="#equipment"
          type="button"
          role="tab"
          aria-controls="equipment"
          aria-selected="false"
        >
          Equipment
        </button>
      </div>
    </nav>
    <div class="tab-content" id="nav-tabContent">
      <!-- character tab -->
      <div
        class="tab-pane fade show active"
        id="character"
        role="tabpanel"
        aria-labelledby="character-tab"
      >
        <div>
          <div :key="character" v-for="character in data">
            {{ character }}
          </div>
          <label for="name">Name</label>
          <input id="name" type="text" />
          <label for="characterLevel">Level</label>
          <input id="characterLevel" type="number" />
          <label for="age">Age</label>
          <input id="age" type="number" />
          <label for="sex">Sex</label>
          <input id="sex" type="radio" />
          <label for="height">Height</label>
          <input id="height" type="number" />
          <label for="weight">Weight</label>
          <input id="weight" type="number" />
          <label for="hair">Hair color</label>
          <input id="hair" type="text" />
          <label for="eye">Eye color</label>
          <input id="eye" type="text" />
          <label for="skinColor">Skin color</label>
          <input id="skinColor" type="text" />
          <label for="backstory">Backstory</label>
          <input id="backstory" type="textfield" />
        </div>
      </div>
      <!-- race tab -->
      <div
        class="tab-pane fade"
        id="race"
        role="tabpanel"
        aria-labelledby="race-tab"
      >
        <label for="races">Select your characters race.</label>
        <div v-bind:key="race.name" v-for="race in races">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="races"
              v-bind:value="race.name"
              v-model="raceSelection"
              @change="getSubRace"
            />
            <label class="form-check-label" for="race.name">
              {{ race.name }}
            </label>
          </div>
        </div>

        <div class="" v-if="subRaces">
          <label for="subraceSelection">Select Subrace</label>
          <select
            class="form-select"
            v-model="subraceSelection"
            id="subraceSelection"
          >
            <option v-bind:key="subRace.name" v-for="subRace in subRaces">
              {{ subRace.name }}
            </option>
          </select>
        </div>

        <div class="" v-else-if="dragonAncestory">
          <label for="subraceSelection">Select Dragon Ancestory</label>
          <select
            class="form-select"
            v-model="subraceSelection"
            id="subraceSelection"
          >
            <option v-bind:key="dragon.name" v-for="dragon in dragonAncestory">
              {{ dragon.name }}
            </option>
          </select>
        </div>
      </div>
      <!-- class tab -->
      <div
        class="tab-pane fade"
        id="class"
        role="tabpanel"
        aria-labelledby="class-tab"
      >
        <div v-bind:key="clas.name" v-for="clas in classes">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="classes"
              v-bind:value="clas.name"
              v-model="classSelection"
              @change="getSubClass"
            />
            <label class="form-check-label" for="clas.name">
              {{ clas.name }}
            </label>
          </div>
        </div>
        <hr />
        <div v-bind:key="subClass.name" v-for="subClass in subClasses">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="classes"
              v-bind:value="subClass.name"
              v-model="subClassSelection"
            />
            <label class="form-check-label" for="subClass.name">
              {{ subClass.name }}
            </label>
          </div>
        </div>
      </div>

      <div
        class="tab-pane fade"
        id="abilityScores"
        role="tabpanel"
        aria-labelledby="abilityScores-tab"
      >
        <div class="row text-center">
          <span :key="ability" v-for="ability in abilityScores" class="col-2">{{
            ability.name
          }}</span>
          <span :key="ability" v-for="ability in abilityScores" class="col-2">
            <input
              @change="setStats(ability)"
              v-model="ability.value"
              type="number"
            />
          </span>
        </div>
        <div v-if="raceSelection === 'Half-Elf'">
          <p>Select 2 abilities</p>
          <span :key="ability.value" v-for="ability in abilityScores">
            <input
              class="mx-2"
              type="checkbox"
              v-bind:value="ability.index"
              v-model="halfElfAbilities"
              v-bind:disabled="
                halfElfAbilities.length === 2 &&
                halfElfAbilities.indexOf(ability.index) == -1
              "
            />
            <label for="ability.name">{{ ability.name }}</label>
          </span>
        </div>
      </div>
      <div
        class="tab-pane fade"
        id="background"
        role="tabpanel"
        aria-labelledby="background-tab"
      >
        <div>
          <label for="alignmentSelection">Select Alignment</label>
          <select class="form-select" v-model="alignmentSelection">
            <option :key="alignment" v-for="alignment in alignments">
              {{ alignment.name }}
            </option>
          </select>
        </div>
        <div v-bind:key="background.name" v-for="background in backgrounds">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="backgrounds"
              v-bind:value="background.name"
              v-model="background.name"
            />
            <label class="form-check-label" for="background.name">
              {{ background.name }}
            </label>
          </div>
        </div>
      </div>
      <div
        class="tab-pane fade"
        id="proficiency"
        role="tabpanel"
        aria-labelledby="proficiency-tab"
      ></div>
      <div
        class="tab-pane fade"
        id="spells"
        role="tabpanel"
        aria-labelledby="spells-tab"
      >
        spells
      </div>
      <div
        class="tab-pane fade"
        id="equipment"
        role="tabpanel"
        aria-labelledby="equipment-tab"
      >
        equipment
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle";
import { mapState } from "vuex";

// @ is an alias to /src
const url = "https://www.dnd5eapi.co/api/";
export default {
  name: "App",
  components: {},
  computed: mapState(["data"]),
  data() {
    return {
      races: [],
      subRaces: null,
      dragonAncestory: null,
      classes: [],
      subClasses: null,
      abilityScores: null,
      halfElfAbilities: [],
      feats: null,
      alignments: null,
      backgrounds: null,
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
      proficiencyChoices: null,
      amountOfProficiencies: 1,
      languageToolProficiencies: null,
      cantrips: null,
      equipment: null,

      name: null,
      characterLevel: 1,
      age: 1,
      sex: null,
      height: 1,
      weight: 1,
      hair: null,
      eye: null,
      skinColor: null,
      backstory: null,
      armorClass: 1,
      hitPoints: 1,
      Speed: 1,
      passivePerception: 1,
      darkVision: 1,
      background: null,
      raceSelection: null,
      subClassSelection: null,
      classSelection: null,
      subRaceSelection: null,
      alignmentSelection: null,
      proficiencySelection: [],
      characterAbilityScores: {
        cha: 0,
        con: 0,
        dex: 0,
        int: 0,
        str: 0,
        wis: 0,
      },
      languageToolProficienciesSelection: null,
      cantripsSelection: null,
      equipment: null,
      testapi: null,
    };
  },
  methods: {
    getRaces() {
      axios({
        method: "get",
        url: url + "races",
      }).then((response) => {
        this.races = response.data.results;
      });
    },

    getSubRace() {
      this.subRaces = null;
      if (this.raceSelection === "Dragonborn") {
        axios({
          method: "get",
          url: url + "traits/draconic-ancestry",
        }).then((response) => {
          this.dragonAncestory =
            response.data.trait_specific.subtrait_options.from;
          if (this.dragonAncestory.length < 1) {
            this.dragonAncestory = null;
          }
        });
      } else {
        this.dragonAncestory = null;
        axios({
          method: "get",
          url: url + "races/" + this.raceSelection.toLowerCase() + "/subraces",
        }).then((response) => {
          this.subRaces = response.data.results;
          if (this.subRaces.length < 1) {
            this.subRaces = null;
          }
        });
      }
    },

    getClasses() {
      axios({
        method: "get",
        url: url + "classes",
      }).then((response) => {
        this.classes = response.data.results;
      });
    },
    getSubClass() {
      axios({
        method: "get",
        url: url + "classes/" + this.classSelection.toLowerCase(),
      }).then((response) => {
        this.subClasses = response.data.subclasses;
      });
    },
    getAbilityScores() {
      axios({
        method: "get",
        url: url + "ability-scores",
      }).then((response) => {
        this.abilityScores = response.data.results;
      });
    },
    getAlignments() {
      axios({
        method: "get",
        url: url + "alignments",
      }).then((response) => {
        this.alignments = response.data.results;
      });
    },
    getBackgrounds() {
      axios({
        method: "get",
        url: url + "backgrounds",
      }).then((response) => {
        this.backgrounds = response.data.results;
      });
    },
    raceBonus() {
      let first = this.halfElfAbilities[0];
      let second = this.halfElfAbilities[1];
      switch (this.raceSelection) {
        case this.races[0].name:
          //dragonborn
          this.charStats.str += 2;
          this.charStats.cha += 1;
          break;
        case this.races[1].name:
          //dwarf

          this.charStats.con += 2;
          break;
        case this.races[2].name:
          //elf

          this.charStats.dex += 2;
          break;
        case this.races[3].name:
          //gnome

          this.charStats.int += 2;
          break;
        case this.races[4].name:
          //half-elf

          this.charStats.cha += 2;
          if (first === "con" || second === "con") {
            this.charStats.con += 1;
          }
          if (first === "dex" || second === "dex") {
            this.charStats.dex += 1;
          }
          break;
        case this.races[5].name:
          //halfling

          this.charStats.dex += 2;
          break;
        case this.races[6].name:
          //half-orc

          this.charStats.str += 2;
          this.charStats.con += 1;
          break;
        case this.races[7].name:
          //human

          this.charStats.cha += 1;
          this.charStats.con += 1;
          this.charStats.dex += 1;
          this.charStats.int += 1;
          this.charStats.str += 1;
          this.charStats.wis += 1;
          break;
        case this.races[8].name:
          //tiefling

          this.charStats.cha += 2;
          this.charStats.int += 2;
      }
    },
  },
  created() {
    this.getRaces();
    this.getClasses();
    this.getAbilityScores();
    this.getAlignments();
    this.getBackgrounds();

    axios({
      method: "get",
      url: "http://127.0.0.1:5050/characters/",
      headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
    })
      .then((response) => {
        this.$store.state.data = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

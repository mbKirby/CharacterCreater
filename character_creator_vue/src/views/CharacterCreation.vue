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
          {{ userId }}
          {{ username }}
          <div>
            <label for="name">Name</label>
            <input v-model="name" id="name" type="text" />
          </div>
          <div>
            <label for="characterLevel">Level</label>
            <input v-model="characterLevel" id="characterLevel" type="number" />
          </div>
          <div>
            <label for="age">Age</label>
            <input v-model="age" id="age" type="number" />
          </div>
          <div>
            <label for="gender">Gender </label>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                name="gender"
                id="Female"
                value="female"
                v-model="sex"
              />
              <label class="form-check-label" for="Female"> Female </label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                name="gender"
                id="male"
                value="male"
                v-model="sex"
              />
              <label class="form-check-label" for="male"> Male </label>
            </div>
          </div>
          <div>
            <label for="height">Height</label>
            <input v-model="height" id="height" type="number" />
          </div>
          <div>
            <label for="weight">Weight</label>
            <input v-model="weight" id="weight" type="number" />
          </div>
          <div>
            <label for="hair">Hair color</label>
            <input v-model="hair" id="hair" type="text" />
          </div>
          <div>
            <label for="eye">Eye color</label>
            <input v-model="eye" id="eye" type="text" />
          </div>
          <div>
            <label for="skinColor">Skin color</label>
            <input v-model="skinColor" id="skinColor" type="text" />
          </div>
          <div>
            <label for="backstory">Backstory</label>
            <input v-model="backstory" id="backstory" type="textfield" />
          </div>
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
          <label for="subRaceSelection">Select Subrace</label>
          <select
            class="form-select"
            v-model="subRaceSelection"
            id="subRaceSelection"
          >
            <option v-bind:key="subRace.name" v-for="subRace in subRaces">
              {{ subRace.name }}
            </option>
          </select>
        </div>

        <div class="" v-else-if="dragonAncestory">
          <label for="subRaceSelection">Select Dragon Ancestory</label>
          <select
            class="form-select"
            v-model="subRaceSelection"
            id="subRaceSelection"
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
              @change="
                getSubClass();
                getProficiencyChoices();
                getEquipment();
              "
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
              name="subClasses"
              v-bind:value="subClass.name"
              v-model="subClassSelection"
            />
            <label class="form-check-label" for="subClass.name">
              {{ subClass.name }}
            </label>
          </div>
        </div>
      </div>
      <!-- Ability Scores tab -->
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
              @change="setAbility(ability)"
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
      <!-- Background tab -->
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
        <div v-bind:key="backgroun.name" v-for="backgroun in backgrounds">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="backgrounds"
              v-bind:value="backgroun.name"
              v-model="background"
            />
            <label class="form-check-label" for="background.name">
              {{ backgroun.name }}
            </label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="backgrounds"
              v-bind:value="backgroun.name"
              v-model="background"
            />
            <label class="form-check-label" for="background.name">
              {{ backgroun.name }}
            </label>
          </div>
        </div>
      </div>
      <!-- proficiency tab -->
      <div
        class="tab-pane fade"
        id="proficiency"
        role="tabpanel"
        aria-labelledby="proficiency-tab"
      >
        <div>
          <p v-if="proficiencyChoices">
            Select {{ amountOfProficiencies }} Proficiencies
          </p>
          <span :key="proficiency" v-for="proficiency in proficiencyChoices">
            <input
              class="mx-2"
              type="checkbox"
              v-bind:value="proficiency.name.substr(7)"
              v-model="proficiencySelection"
              v-bind:disabled="
                proficiencySelection.length === amountOfProficiencies &&
                proficiencySelection.indexOf(proficiency.name.substr(7)) == -1
              "
            />
            <label for="proficiency.name">{{
              proficiency.name.substr(7)
            }}</label>
          </span>
        </div>
      </div>
      <!-- Spells tab -->
      <div
        class="tab-pane fade"
        id="spells"
        role="tabpanel"
        aria-labelledby="spells-tab"
      >
        spells
      </div>
      <!-- Equipment tab -->
      <div
        class="tab-pane fade"
        id="equipment"
        role="tabpanel"
        aria-labelledby="equipment-tab"
        :key="equip"
        v-for="equip in equipments"
      >
        <!-- <p>Select {{ equip.choose }} from the list</p>
        <div :key="item" v-for="item in equip.from">
          {{ item.equipment.name }}
          {{ item.equipment_option }}
        </div>
        {{ equip.from[0].equipment.name }} -->
      </div>
    </div>
    <hr />
    <div class="text-center">
      <button
        :disabled="!this.$store.getters.loggedIn"
        class="btn btn-dark"
        type="submit"
        @click="createCharacter()"
      >
        Create Character
      </button>
      <button @click="test()">test</button>
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
  computed: mapState(["data", "username"]),
  data() {
    return {
      userId: this.$store.state.username,

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
      equipments: null,
      item: null,

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
      languageToolProficienciesSelection: "dwarfish",
      cantripsSelection: "lights",
      equipmentSelection: "longsword",
      testapi: null,
    };
  },
  methods: {
    test() {
      console.log(this.username[0].id);
    },
    getUser() {
      axios({
        method: "get",
        url: "http://127.0.0.1:5050/user/",
        headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
      })
        .then((response) => {
          this.$store.state.username = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
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
    getProficiencyChoices() {
      this.amountOfProficiencies = [];
      axios({
        method: "get",
        url: url + "classes/" + this.classSelection.toLowerCase(),
      }).then((response) => {
        if (this.classSelection === "Monk") {
          this.proficiencyChoices = response.data.proficiencySelection[2].from;
          this.amountOfProficiencies =
            response.data.proficiencySelection[2].choose;
        } else {
          this.proficiencyChoices = response.data.proficiency_choices[0].from;
          this.amountOfProficiencies =
            response.data.proficiency_choices[0].choose;
        }
      });
    },
    getEquipment() {
      axios({
        method: "get",
        url: url + "classes/" + this.classSelection.toLowerCase(),
      }).then((response) => {
        this.equipments = response.data.starting_equipment_options;
      });
      console.log(this.equipment);
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
    raceBonus() {
      let first = this.halfElfAbilities[0];
      let second = this.halfElfAbilities[1];
      switch (this.raceSelection) {
        case this.races[0].name:
          //dragonborn
          this.characterAbilityScores.str += 2;
          this.characterAbilityScores.cha += 1;
          break;
        case this.races[1].name:
          //dwarf

          this.characterAbilityScores.con += 2;
          break;
        case this.races[2].name:
          //elf

          this.characterAbilityScores.dex += 2;
          break;
        case this.races[3].name:
          //gnome

          this.characterAbilityScores.int += 2;
          break;
        case this.races[4].name:
          //half-elf

          this.characterAbilityScores.cha += 2;

          if (first === "con" || second === "con") {
            this.characterAbilityScores.con += 1;
          }
          if (first === "dex" || second === "dex") {
            this.characterAbilityScores.dex += 1;
          }
          if (first === "int" || second === "int") {
            this.characterAbilityScores.int += 1;
          }
          if (first === "str" || second === "str") {
            this.characterAbilityScores.str += 1;
          }
          if (first === "wis" || second === "wis") {
            this.characterAbilityScores.wis += 1;
          }
          break;
        case this.races[5].name:
          //halfling

          this.characterAbilityScores.dex += 2;
          break;
        case this.races[6].name:
          //half-orc

          this.characterAbilityScores.str += 2;
          this.characterAbilityScores.con += 1;
          break;
        case this.races[7].name:
          //human

          this.characterAbilityScores.cha += 1;
          this.characterAbilityScores.con += 1;
          this.characterAbilityScores.dex += 1;
          this.characterAbilityScores.int += 1;
          this.characterAbilityScores.str += 1;
          this.characterAbilityScores.wis += 1;
          break;
        case this.races[8].name:
          //tiefling

          this.characterAbilityScores.cha += 2;
          this.characterAbilityScores.int += 2;
      }
    },
    setAbility(ability) {
      if (ability.name.toLowerCase() === "cha") {
        this.characterAbilityScores.cha = ability.value;
      }
      if (ability.name.toLowerCase() === "con") {
        this.characterAbilityScores.con = ability.value;
      }
      if (ability.name.toLowerCase() === "dex") {
        this.characterAbilityScores.dex = ability.value;
      }
      if (ability.name.toLowerCase() === "int") {
        this.characterAbilityScores.int = ability.value;
      }
      if (ability.name.toLowerCase() === "str") {
        this.characterAbilityScores.str = ability.value;
      }
      if (ability.name.toLowerCase() === "wis") {
        this.characterAbilityScores.wis = ability.value;
      }
      console.log(this.characterAbilityScores);
    },
    proficiencyBonus() {
      for (let i = 0; i < this.chosenProficiencies.length; i++) {
        switch (this.chosenProficiencies[i]) {
          case Object.keys(this.proficiencies.cha[0])[0]:
            this.proficiencies.cha[0].Deception += 3;
            break;
          case Object.keys(this.proficiencies.cha[1])[0]:
            this.proficiencies.cha[1].Intimidation += 3;
            break;
          case Object.keys(this.proficiencies.cha[2])[0]:
            this.proficiencies.cha[2].Performance += 3;
            break;
          case Object.keys(this.proficiencies.cha[3])[0]:
            this.proficiencies.cha[3].Persuasion += 3;
            break;
          // End of cha
          case Object.keys(this.proficiencies.dex[0])[0]:
            this.proficiencies.dex[0].Acrobatics += 3;
            break;
          case Object.keys(this.proficiencies.dex[1])[0]:
            this.proficiencies.dex[1]["Sleight of Hand"] += 3;
            break;
          case Object.keys(this.proficiencies.dex[2])[0]:
            this.proficiencies.dex[2].Stealth += 3;
            break;
          // End of dex
          case Object.keys(this.proficiencies.int[0])[0]:
            this.proficiencies.int[0].Arcana += 3;
            break;
          case Object.keys(this.proficiencies.int[1])[0]:
            this.proficiencies.int[1].History += 3;
            break;
          case Object.keys(this.proficiencies.int[2])[0]:
            this.proficiencies.int[2].Investigation += 3;
            break;
          case Object.keys(this.proficiencies.int[3])[0]:
            this.proficiencies.int[3].Nature += 3;
            break;
          case Object.keys(this.proficiencies.int[4])[0]:
            this.proficiencies.int[4].Religion += 3;
            break;
          //end of int
          case Object.keys(this.proficiencies.str[0])[0]:
            this.proficiencies.str[0].Athletics += 3;
            console.log("strength chack");
            break;
          //end of str
          case Object.keys(this.proficiencies.wis[0])[0]:
            this.proficiencies.wis[0]["Animal Handling"] += 3;
            break;
          case Object.keys(this.proficiencies.wis[1])[0]:
            this.proficiencies.wis[1].Insight += 3;
            break;
          case Object.keys(this.proficiencies.wis[2])[0]:
            this.proficiencies.wis[2].Medicine += 3;
            break;
          case Object.keys(this.proficiencies.wis[3])[0]:
            this.proficiencies.wis[3].Perception += 3;
            break;
          case Object.keys(this.proficiencies.wis[4])[0]:
            this.proficiencies.wis[4].Survival += 3;
            break;
        }
      }
    },
    armorClass() {
      this.armorClass = 10 + this.savingThrows(this.characterAbilityScores.dex);
    },
    convertToString(list) {
      let newList = list.join();
      return newList;
    },
    createCharacter() {
      this.armorClass();
      this.raceBonus();
      axios({
        method: "post",
        url: "http://127.0.0.1:5050/characters/",
        headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        data: {
          user: this.username[0].id,
          name: this.name,
          characterLevel: this.characterLevel,
          age: this.age,
          sex: this.sex,
          height: this.height,
          weight: this.weight,
          hair: this.hair,
          eye: this.eye,
          skinColor: this.skinColor,
          backstory: this.backstory,
          armorClass: this.armorClass,
          hitPoints: this.hitPoints,
          Speed: this.Speed,
          passivePerception: this.passivePerception,
          darkVision: this.darkVision,
          background: this.background,
          raceSelection: this.raceSelection,
          subRaceSelection: this.subRaceSelection,
          classSelection: this.classSelection,
          subClassSelection: this.subClassSelection,
          alignmentSelection: this.alignmentSelection,
          chosenProficiencies: this.convertToString(this.proficiencySelection),
          cha: this.characterAbilityScores.cha,
          con: this.characterAbilityScores.con,
          dex: this.characterAbilityScores.dex,
          int: this.characterAbilityScores.int,
          str: this.characterAbilityScores.str,
          wis: this.characterAbilityScores.wis,
          languageToolProficienciesSelection:
            this.languageToolProficienciesSelection,
          cantripsSelection: this.cantripsSelection,
          equipment: this.equipmentSelection,
        },
      }).then(() => {
        this.$router.push({ name: "CharacterSheet" });
      });
    },
  },
  created() {
    this.getRaces();
    this.getClasses();
    this.getAbilityScores();
    this.getAlignments();
    this.getBackgrounds();
    this.getUser();

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
